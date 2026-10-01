"""
Exploratory analyses for the AI Discernment survey experiment.
E1: Heterogeneity by ChatGPT usage (interaction with total_score)
E2: Robustness excluding attention-check failures (pk_score == 0)
E3: Decomposition by media type (video vs. image scores)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# ─── Setup ───────────────────────────────────────────────────────────────────
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)

df = pd.read_csv("data/clean.csv")

ARM_LABELS = {
    0: "Control", 1: "Flagging", 2: "Provenance", 3: "Automated Flagging",
    4: "AI Accuracy Nudge", 5: "Breathing Exercise", 6: "Mindfulness",
    7: "Inoculation", 8: "AI Literacy Infographic", 9: "AI Literacy Infographic 2",
    10: "AI Literacy Guide", 11: "AI Text Video"
}

# ─── E1: Heterogeneity by ChatGPT usage ─────────────────────────────────────
# Rationale: AI literacy interventions may be more effective for those without
# prior AI experience; testing the arm × chatgpt interaction identifies which
# subgroups benefit most.

df_e1 = df.dropna(subset=["total_score", "chatgpt"]).copy()
df_e1["chatgpt"] = (df_e1["chatgpt"] == 1).astype(int)

formula_e1 = "total_score ~ C(arm_code, Treatment(reference=0)) * C(chatgpt)"
model_e1 = smf.wls(formula_e1, data=df_e1, weights=df_e1["ipw"]).fit(cov_type="HC2")

# Extract interaction terms (arm × chatgpt=1)
rows_e1 = []
for arm in range(1, 12):
    term = f"C(arm_code, Treatment(reference=0))[T.{arm}]:C(chatgpt)[T.1]"
    if term in model_e1.params.index:
        est = model_e1.params[term]
        se = model_e1.bse[term]
        p = model_e1.pvalues[term]
        ci = model_e1.conf_int().loc[term]
        rows_e1.append({
            "arm_code": arm,
            "arm_label": ARM_LABELS[arm],
            "estimate": round(est, 4),
            "std_error": round(se, 4),
            "p_value": round(p, 4),
            "conf_low": round(ci[0], 4),
            "conf_high": round(ci[1], 4),
        })

tab_e1 = pd.DataFrame(rows_e1)
tab_e1.to_csv("results/E1_chatgpt_heterogeneity.csv", index=False)

# Summary: how many significant interactions
n_sig_e1 = (tab_e1["p_value"] < 0.05).sum()
print(f"E1: {n_sig_e1}/10 arms show significant arm×ChatGPT interaction on total_score (HC2, IPW).")

# Figure E1: forest plot of interaction terms
fig, ax = plt.subplots(figsize=(7, 5))
y_pos = np.arange(len(tab_e1))
ax.hlines(y_pos, tab_e1["conf_low"], tab_e1["conf_high"], color="#2b2b2b", lw=1.2)
ax.scatter(tab_e1["estimate"], y_pos, color="#c0392b", s=30, zorder=3)
ax.axvline(0, color="#888888", lw=0.8, ls="--")
ax.set_yticks(y_pos)
ax.set_yticklabels(tab_e1["arm_label"], fontsize=9)
ax.set_xlabel("Interaction effect (arm × ChatGPT user) on total_score", fontsize=10)
ax.set_title("E1: Heterogeneity by ChatGPT usage", fontsize=11, loc="left")
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#2b2b2b")
ax.tick_params(left=False)
fig.tight_layout()
fig.savefig("figures/E1_chatgpt_heterogeneity.png", dpi=200)
plt.close(fig)

# ─── E2: Robustness excluding attention-check failures ──────────────────────
# Rationale: Excluding respondents who failed both attention checks (pk_score=0)
# tests whether registered results are driven by inattentive respondents.

df_e2 = df[df["pk_score"] > 0].copy()
n_excluded = len(df) - len(df_e2)

formula_e2 = "total_score ~ C(arm_code, Treatment(reference=0))"
model_e2 = smf.wls(formula_e2, data=df_e2, weights=df_e2["ipw"]).fit(cov_type="HC2")

rows_e2 = []
for arm in range(1, 12):
    term = f"C(arm_code, Treatment(reference=0))[T.{arm}]"
    est = model_e2.params[term]
    se = model_e2.bse[term]
    p = model_e2.pvalues[term]
    ci = model_e2.conf_int().loc[term]
    rows_e2.append({
        "arm_code": arm,
        "arm_label": ARM_LABELS[arm],
        "estimate": round(est, 4),
        "std_error": round(se, 4),
        "p_value": round(p, 4),
        "conf_low": round(ci[0], 4),
        "conf_high": round(ci[1], 4),
    })

tab_e2 = pd.DataFrame(rows_e2)
tab_e2.to_csv("results/E2_no_attention_fail.csv", index=False)

n_sig_e2 = (tab_e2["p_value"] < 0.05).sum()
print(f"E2: After excluding {n_excluded} attention-check failures, {n_sig_e2}/10 arms significant on total_score (HC2, IPW).")

# ─── E3: Decomposition by media type (video vs. image) ──────────────────────
# Rationale: Interventions may differentially affect detection of video vs.
# image content, explaining why some arms improve fake_score but not total_score.

video_items = [
    "johnson_real_003.mp4", "andersoncooper_fake_001.mp4",
    "biden_draft_fake_009.mp4", "biden_fake_003.mp4",
    "desantis_fake_002.mp4", "trump_voice_fake_011.mp4",
    "warren_fake_012.mp4"
]
image_items = [
    "biden2_real_news_005.png", "biden_real_005.png",
    "biden_real_news_001.png", "election_real_news_006.png",
    "google_real_news_003.png", "hot_weather_real_news_008.png",
    "jim_jordan_real_news_007.png", "poland_real_news_002.png",
    "protest_real_news_004.png", "putin_real_002.webp",
    "unhorse_real_004.png", "untrump_real_001.webp",
    "biden_fake_006.png", "trump_arrest_fake_008.png",
    "trump_epstein_fake_010.png", "trump_fake_004.png",
    "trump_fire_fake_007.png"
]

df_e3 = df.copy()
df_e3["video_score"] = df_e3[video_items].mean(axis=1)
df_e3["image_score"] = df_e3[image_items].mean(axis=1)

rows_e3 = []
for outcome in ["video_score", "image_score"]:
    formula_e3 = f"{outcome} ~ C(arm_code, Treatment(reference=0))"
    model_e3 = smf.wls(formula_e3, data=df_e3, weights=df_e3["ipw"]).fit(cov_type="HC2")
    for arm in range(1, 12):
        term = f"C(arm_code, Treatment(reference=0))[T.{arm}]"
        est = model_e3.params[term]
        se = model_e3.bse[term]
        p = model_e3.pvalues[term]
        ci = model_e3.conf_int().loc[term]
        rows_e3.append({
            "outcome": outcome,
            "arm_code": arm,
            "arm_label": ARM_LABELS[arm],
            "estimate": round(est, 4),
            "std_error": round(se, 4),
            "p_value": round(p, 4),
            "conf_low": round(ci[0], 4),
            "conf_high": round(ci[1], 4),
        })

tab_e3 = pd.DataFrame(rows_e3)
tab_e3.to_csv("results/E3_media_type_decomposition.csv", index=False)

# Summary
vid_sig = tab_e3[(tab_e3["outcome"] == "video_score") & (tab_e3["p_value"] < 0.05)]
img_sig = tab_e3[(tab_e3["outcome"] == "image_score") & (tab_e3["p_value"] < 0.05)]
print(f"E3: {len(vid_sig)}/10 arms significant on video_score; {len(img_sig)}/10 on image_score (HC2, IPW).")

# Figure E3: grouped forest plot (video vs image)
fig, ax = plt.subplots(figsize=(7, 6))
arms = list(range(1, 12))
labels = [ARM_LABELS[a] for a in arms]
y_vid = np.arange(len(arms)) + 0.2
y_img = np.arange(len(arms)) - 0.2

vid_data = tab_e3[tab_e3["outcome"] == "video_score"].set_index("arm_code").loc[arms].reset_index()
img_data = tab_e3[tab_e3["outcome"] == "image_score"].set_index("arm_code").loc[arms].reset_index()

ax.hlines(y_vid, vid_data["conf_low"], vid_data["conf_high"], color="#2b2b2b", lw=1.2)
ax.scatter(vid_data["estimate"], y_vid, color="#c0392b", s=25, zorder=3, label="Video")
ax.hlines(y_img, img_data["conf_low"], img_data["conf_high"], color="#2b2b2b", lw=1.2)
ax.scatter(img_data["estimate"], y_img, color="#2980b9", s=25, zorder=3, label="Image")
ax.axvline(0, color="#888888", lw=0.8, ls="--")
ax.set_yticks(np.arange(len(arms)))
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("Treatment effect (HC2, IPW)", fontsize=10)
ax.set_title("E3: Effect by media type (video vs. image)", fontsize=11, loc="left")
# Direct labels instead of legend
ax.text(vid_data["estimate"].max() + 0.01, y_vid[-1], "Video", fontsize=9, color="#c0392b", va="center")
ax.text(img_data["estimate"].max() + 0.01, y_img[-1], "Image", fontsize=9, color="#2980b9", va="center")
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#2b2b2b")
ax.tick_params(left=False)
fig.tight_layout()
fig.savefig("figures/E3_media_type_decomposition.png", dpi=200)
plt.close(fig)

print("Done: 3 exploratory analyses complete.")
