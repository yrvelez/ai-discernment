"""Exploratory analyses for the AI discernment survey experiment.

E1: Criterion-shift ("say-fake" rate) analysis -- do arms that improved fake
    detection (H2) simply shift respondents toward labeling content as fake?
E2: Heterogeneity of total_score effects by prior generative-AI tool use.
E3: Placebo check -- arms should not predict pre-treatment political knowledge.

All models use IPW weights and HC2 robust standard errors, matching the
registered analyses.
"""
import os
import re

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)

df = pd.read_csv("data/clean.csv")

ARM_LABELS = {
    0: "Control", 1: "Flagging", 2: "Provenance", 3: "Automated Flagging",
    4: "AI Accuracy Nudge", 5: "Breathing Exercise", 6: "Mindfulness",
    7: "Inoculation", 8: "AI Literacy Infographic",
    9: "AI Literacy Infographic 2", 10: "AI Literacy Guide",
    11: "AI Text Video",
}
ARM = "C(arm_code, Treatment(reference=0))"


def tidy(model, analysis_id, keep=None):
    ci = model.conf_int()
    out = pd.DataFrame({
        "analysis_id": analysis_id,
        "term": model.params.index,
        "estimate": model.params.values,
        "std_error": model.bse.values,
        "statistic": model.tvalues.values,
        "p_value": model.pvalues.values,
        "conf_low": ci[0].values,
        "conf_high": ci[1].values,
    })
    if keep is not None:
        out = out[out["term"].isin(keep)].reset_index(drop=True)
    return out


def arm_from_term(term):
    m = re.search(r"\[T\.(\d+)\]", term)
    return int(m.group(1)) if m else np.nan


def add_arm_cols(tab, nobs):
    tab = tab.copy()
    tab["arm_code"] = tab["term"].map(arm_from_term)
    tab = tab.dropna(subset=["arm_code"])
    tab["arm_code"] = tab["arm_code"].astype(int)
    tab["arm_label"] = tab["arm_code"].map(ARM_LABELS)
    tab["n"] = int(nobs)
    cols = ["analysis_id", "arm_code", "arm_label", "term", "estimate",
            "std_error", "statistic", "p_value", "conf_low", "conf_high", "n"]
    return tab[cols].sort_values("arm_code").reset_index(drop=True)


def forest(tab, title, xlabel, path):
    t = tab.sort_values("estimate").reset_index(drop=True)
    y = np.arange(len(t))
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.errorbar(t["estimate"], y,
                xerr=[t["estimate"] - t["conf_low"],
                      t["conf_high"] - t["estimate"]],
                fmt="o", color="black", ecolor="gray", capsize=3, ms=5)
    ax.axvline(0, color="red", ls="--", lw=1)
    ax.set_yticks(y)
    ax.set_yticklabels(t["arm_label"], fontsize=9)
    ax.set_xlabel(xlabel)
    ax.set_title(title, fontsize=10)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# E1: "Say-fake" rate (criterion shift). For fake items, said-fake = response;
# for real items, said-fake = 1 - response. Averaged over all 24 items.
# ---------------------------------------------------------------------------
fake_cols = [c for c in df.columns if "_fake_" in c]
real_cols = [c for c in df.columns if "_real_" in c]
said_fake = pd.concat([df[fake_cols], 1.0 - df[real_cols]], axis=1)
df["say_fake"] = said_fake.mean(axis=1)

d1 = df.dropna(subset=["say_fake"]).copy()
m1 = smf.wls(f"say_fake ~ {ARM}", data=d1,
             weights=d1["ipw"]).fit(cov_type="HC2")
arm_terms1 = [t for t in m1.params.index if t.startswith("C(arm_code")]
t1 = add_arm_cols(tidy(m1, "E1", keep=arm_terms1), m1.nobs)
t1.to_csv("results/E1_say_fake_rate.csv", index=False)
forest(t1, "E1: Effect on propensity to label content AI-generated",
       "Difference in say-fake rate vs control (IPW, HC2)",
       "figures/E1_say_fake_forest.png")

sig1 = t1[t1["p_value"] < 0.05]
top1 = t1.loc[t1["estimate"].idxmax()]
print(f"E1: {len(sig1)}/11 arms significantly shifted the say-fake rate; "
      f"largest shift = {top1['arm_label']} "
      f"({top1['estimate']:+.3f}, p={top1['p_value']:.3f}).")

# ---------------------------------------------------------------------------
# E2: Heterogeneity by prior generative-AI tool use (ai_scale > 0).
# ---------------------------------------------------------------------------
df["ai_user"] = (df["ai_scale"] > 0).astype(int)
d2 = df.dropna(subset=["total_score"]).copy()
m2 = smf.wls(f"total_score ~ {ARM} * ai_user", data=d2,
             weights=d2["ipw"]).fit(cov_type="HC2")
inter_terms = [t for t in m2.params.index if ":ai_user" in t]
t2 = add_arm_cols(tidy(m2, "E2", keep=inter_terms), m2.nobs)
wt2 = m2.wald_test(", ".join(f"{t} = 0" for t in inter_terms))
joint2 = pd.DataFrame({
    "analysis_id": ["E2"], "arm_code": [np.nan], "arm_label": ["JOINT"],
    "term": ["JOINT: all arm x ai_user interactions = 0"],
    "estimate": [np.nan], "std_error": [np.nan],
    "statistic": [float(np.asarray(wt2.statistic))],
    "p_value": [float(wt2.pvalue)],
    "conf_low": [np.nan], "conf_high": [np.nan], "n": [int(m2.nobs)],
})
t2 = pd.concat([t2, joint2], ignore_index=True)
t2.to_csv("results/E2_ai_use_heterogeneity.csv", index=False)
forest(t2[t2["arm_label"] != "JOINT"],
       "E2: Arm x prior-AI-use interactions (total_score)",
       "Interaction estimate vs control (IPW, HC2)",
       "figures/E2_ai_use_interaction_forest.png")

print(f"E2: joint test of arm x prior-AI-use interactions on total_score: "
      f"F={float(np.asarray(wt2.statistic)):.2f}, p={float(wt2.pvalue):.3f}.")

# ---------------------------------------------------------------------------
# E3: Placebo -- arms should not predict pre-treatment political knowledge.
# ---------------------------------------------------------------------------
d3 = df.dropna(subset=["pk_score"]).copy()
m3 = smf.wls(f"pk_score ~ {ARM}", data=d3,
             weights=d3["ipw"]).fit(cov_type="HC2")
arm_terms3 = [t for t in m3.params.index if t.startswith("C(arm_code")]
t3 = add_arm_cols(tidy(m3, "E3", keep=arm_terms3), m3.nobs)
wt3 = m3.wald_test(", ".join(f"{t} = 0" for t in arm_terms3))
joint3 = pd.DataFrame({
    "analysis_id": ["E3"], "arm_code": [np.nan], "arm_label": ["JOINT"],
    "term": ["JOINT: all arm dummies = 0"],
    "estimate": [np.nan], "std_error": [np.nan],
    "statistic": [float(np.asarray(wt3.statistic))],
    "p_value": [float(wt3.pvalue)],
    "conf_low": [np.nan], "conf_high": [np.nan], "n": [int(m3.nobs)],
})
t3 = pd.concat([t3, joint3], ignore_index=True)
t3.to_csv("results/E3_placebo_pk.csv", index=False)

print(f"E3: placebo joint test of arm dummies on pre-treatment pk_score: "
      f"F={float(np.asarray(wt3.statistic)):.2f}, p={float(wt3.pvalue):.3f}.")
