"""
Exploratory analyses for the AI Discernment survey experiment.
Three analyses:
  E1: Heterogeneity by political interest (low vs high) on total_score
  E2: Robustness to attention-check failures (exclude pk_score == 0)
  E3: AI familiarity (ai_scale) as a moderator of treatment effects
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)

# ── Load ──────────────────────────────────────────────────────────────────────
df = pd.read_csv("data/clean.csv")
df["arm_str"] = df["arm_code"].astype(str)

ARM_LABELS = {
    "1": "Flagging", "2": "Provenance", "3": "Automated Flagging",
    "4": "AI Accuracy Nudge", "5": "Breathing Exercise", "6": "Mindfulness",
    "7": "Inoculation", "8": "AI Lit. Infographic", "9": "AI Lit. Infographic 2",
    "10": "AI Literacy Guide", "11": "AI Text Video"
}

# ── E1: Heterogeneity by political interest ──────────────────────────────────
# Rationale: More politically interested respondents may be more (or less)
# responsive to AI-literacy interventions, which would help interpret whether
# the registered effects are driven by a motivated subset.
# Method: OLS total_score ~ arm dummies, separately for low (1-3) and high (4-5)
# political interest, HC2 robust SEs.

df["pol_group"] = np.where(df["political_interest"] <= 3, "low", "high")

rows_e1 = []
for grp in ["low", "high"]:
    sub = df[df["pol_group"] == grp].copy()
    m = smf.ols("total_score ~ C(arm_str, Treatment(reference='0'))", data=sub).fit(cov_type="HC2")
    ci = m.conf_int()
    for arm in range(1, 12):
        term = f"C(arm_str, Treatment(reference='0'))[T.{arm}]"
        if term in m.params.index:
            rows_e1.append({
                "group": grp, "arm": arm, "arm_label": ARM_LABELS[str(arm)],
                "estimate": m.params[term], "std_error": m.bse[term],
                "p_value": m.pvalues[term],
                "conf_low": ci.loc[term, 0], "conf_high": ci.loc[term, 1],
                "n": int(m.nobs)
            })

e1_df = pd.DataFrame(rows_e1)
e1_df.to_csv("results/E1_political_interest_heterogeneity.csv", index=False)

# Summary line for E1
sig_e1 = e1_df[e1_df["p_value"] < 0.05].sort_values("p_value")
if len(sig_e1):
    top = sig_e1.iloc[0]
    e1_summary = (f"E1: Political-interest heterogeneity — {len(sig_e1)} significant effects; "
                  f"strongest: {top['arm_label']} in {top['group']}-interest group "
                  f"({top['estimate']:+.3f}, p={top['p_value']:.3f})")
else:
    e1_summary = "E1: Political-interest heterogeneity — no significant effects at p<0.05 in either group"
print(e1_summary)

# Figure E1: forest plot
fig, ax = plt.subplots(figsize=(9, 7))
y_pos = {}
for i, (grp, offset) in enumerate([("low", -0.18), ("high", 0.18)]):
    sub = e1_df[e1_df["group"] == grp].sort_values("arm")
    for j, (_, r) in enumerate(sub.iterrows()):
        y = (11 - r["arm"]) + offset
        color = "#2171b5" if grp == "low" else "#d94801"
        ax.errorbar(r["estimate"], y,
                    xerr=[[r["estimate"] - r["conf_low"]], [r["conf_high"] - r["estimate"]]],
                    fmt="o", color=color, ms=5, capsize=3, lw=1.2)
        y_pos[(grp, r["arm"])] = y

ax.axvline(0, color="#333", lw=0.8, ls="--")
ax.set_yticks([(11 - a) for a in range(1, 12)])
ax.set_yticklabels([ARM_LABELS[str(a)] for a in range(1, 12)], fontsize=9)
ax.set_xlabel("Treatment effect on total_score (95% CI)", fontsize=10)
ax.set_title("E1: Treatment effects by political interest", fontsize=11, pad=10)

# Direct labels instead of legend
ax.plot([], [], "o", color="#2171b5", ms=5, label="_nolegend_")
ax.plot([], [], "o", color="#d94801", ms=5, label="_nolegend_")
ax.text(0.98, 0.02, "● Low interest (1–3)\n● High interest (4–5)",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=8,
        color="#333",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#ccc", lw=0.5))
# color the text dots
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#333")
ax.tick_params(colors="#333")
fig.tight_layout()
fig.savefig("figures/E1_political_interest_forest.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ── E2: Robustness to attention-check failures ───────────────────────────────
# Rationale: Excluding respondents who failed both attention checks (pk_score=0)
# tests whether the registered treatment effects are inflated by inattentive
# respondents who guessed randomly.
# Method: OLS total_score ~ arm dummies on the subset with pk_score > 0, HC2 SEs.
# Also report the full-sample estimates side-by-side for comparison.

n_excl = int((df["pk_score"] == 0).sum())
sub_e2 = df[df["pk_score"] > 0].copy()

m_full = smf.ols("total_score ~ C(arm_str, Treatment(reference='0'))", data=df).fit(cov_type="HC2")
m_excl = smf.ols("total_score ~ C(arm_str, Treatment(reference='0'))", data=sub_e2).fit(cov_type="HC2")
ci_full = m_full.conf_int()
ci_excl = m_excl.conf_int()

rows_e2 = []
for arm in range(1, 12):
    term = f"C(arm_str, Treatment(reference='0'))[T.{arm}]"
    if term in m_excl.params.index:
        rows_e2.append({
            "arm": arm, "arm_label": ARM_LABELS[str(arm)],
            "est_full": m_full.params[term], "se_full": m_full.bse[term],
            "p_full": m_full.pvalues[term],
            "est_excl": m_excl.params[term], "se_excl": m_excl.bse[term],
            "p_excl": m_excl.pvalues[term],
            "ci_excl_low": ci_excl.loc[term, 0], "ci_excl_high": ci_excl.loc[term, 1],
            "n_full": int(m_full.nobs), "n_excl": int(m_excl.nobs)
        })

e2_df = pd.DataFrame(rows_e2)
e2_df.to_csv("results/E2_attention_check_robustness.csv", index=False)

# Summary: how many flip significance?
flips = e2_df[((e2_df["p_full"] < 0.05) & (e2_df["p_excl"] >= 0.05)) |
              ((e2_df["p_full"] >= 0.05) & (e2_df["p_excl"] < 0.05))]
sig_excl = e2_df[e2_df["p_excl"] < 0.05]
e2_summary = (f"E2: Attention-check robustness — excluded {n_excl} respondents (pk_score=0); "
              f"{len(sig_excl)} arms still significant after exclusion; "
              f"{len(flips)} significance flips")
print(e2_summary)

# ── E3: AI familiarity as moderator ──────────────────────────────────────────
# Rationale: Respondents with higher prior AI-tool familiarity (ai_scale) may
# respond differently to AI-literacy interventions; this interaction helps
# distinguish whether interventions work by providing new information or by
# changing behaviour regardless of prior knowledge.
# Method: OLS total_score ~ arm dummies × centered ai_scale, HC2 SEs.
# Report the interaction terms (arm × ai_scale_c).

df["ai_scale_c"] = df["ai_scale"] - df["ai_scale"].mean()
m_e3 = smf.ols(
    "total_score ~ C(arm_str, Treatment(reference='0')) * ai_scale_c",
    data=df
).fit(cov_type="HC2")
ci_e3 = m_e3.conf_int()

rows_e3 = []
for arm in range(1, 12):
    term = f"C(arm_str, Treatment(reference='0'))[T.{arm}]:ai_scale_c"
    if term in m_e3.params.index:
        rows_e3.append({
            "arm": arm, "arm_label": ARM_LABELS[str(arm)],
            "estimate": m_e3.params[term], "std_error": m_e3.bse[term],
            "p_value": m_e3.pvalues[term],
            "conf_low": ci_e3.loc[term, 0], "conf_high": ci_e3.loc[term, 1],
            "n": int(m_e3.nobs)
        })

e3_df = pd.DataFrame(rows_e3)
e3_df.to_csv("results/E3_ai_familiarity_moderation.csv", index=False)

sig_e3 = e3_df[e3_df["p_value"] < 0.05].sort_values("p_value")
if len(sig_e3):
    top3 = sig_e3.iloc[0]
    e3_summary = (f"E3: AI-familiarity moderation — {len(sig_e3)} significant interactions; "
                  f"strongest: {top3['arm_label']} × ai_scale "
                  f"({top3['estimate']:+.4f}, p={top3['p_value']:.4f})")
else:
    e3_summary = "E3: AI-familiarity moderation — no significant arm × ai_scale interactions at p<0.05"
print(e3_summary)

# Figure E3: forest plot of interaction terms
fig, ax = plt.subplots(figsize=(8, 6))
e3_sorted = e3_df.sort_values("arm")
for _, r in e3_sorted.iterrows():
    y = 11 - r["arm"]
    color = "#d94801" if r["p_value"] < 0.05 else "#666"
    ax.errorbar(r["estimate"], y,
                xerr=[[r["estimate"] - r["conf_low"]], [r["conf_high"] - r["estimate"]]],
                fmt="o", color=color, ms=5, capsize=3, lw=1.2)

ax.axvline(0, color="#333", lw=0.8, ls="--")
ax.set_yticks([(11 - a) for a in range(1, 12)])
ax.set_yticklabels([ARM_LABELS[str(a)] for a in range(1, 12)], fontsize=9)
ax.set_xlabel("Interaction coefficient (arm × ai_scale_c, 95% CI)", fontsize=10)
ax.set_title("E3: AI familiarity moderates treatment effects on total_score", fontsize=11, pad=10)
ax.text(0.98, 0.02, "● p < 0.05\n● p ≥ 0.05",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=8,
        color="#333",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#ccc", lw=0.5))
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#333")
ax.tick_params(colors="#333")
fig.tight_layout()
fig.savefig("figures/E3_ai_familiarity_interaction.png", dpi=200, bbox_inches="tight")
plt.close(fig)

print("Done. Wrote 3 CSVs and 2 figures.")
