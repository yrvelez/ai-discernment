"""
Exploratory analyses for the AI Discernment survey experiment.
Three pre-specified exploratory checks to interpret registered results.
"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
os.makedirs('results', exist_ok=True)
os.makedirs('figures', exist_ok=True)

df = pd.read_csv('data/clean.csv')
df['arm_code'] = df['arm_code'].astype(int)

arm_labels = {
    0: 'Control', 1: 'Flagging', 2: 'Provenance', 3: 'Automated Flagging',
    4: 'AI Accuracy Nudge', 5: 'Breathing Exercise', 6: 'Mindfulness',
    7: 'Inoculation', 8: 'AI Literacy Infographic', 9: 'AI Literacy Infographic 2',
    10: 'AI Literacy Guide', 11: 'AI Text Video'
}

ACCENT = '#C0392B'
INK = '#2C3E50'

# ── E1: Attention-check exclusion robustness ──────────────────────────────────
# Rationale: Excluding respondents who failed both attention checks (pk_score == 0)
# tests whether registered null results are inflated by inattentive respondents.
print("=" * 60)
print("E1: Attention-check exclusion robustness (H1: total_score)")
print("=" * 60)

df_e1 = df[df['pk_score'] > 0].copy()
n_excluded = len(df) - len(df_e1)

formula_e1 = 'total_score ~ C(arm_code, Treatment(reference=0))'
model_e1 = smf.wls(formula_e1, data=df_e1, weights=df_e1['ipw']).fit(cov_type='HC2')

rows_e1 = []
for arm in range(1, 12):
    term = f'C(arm_code, Treatment(reference=0))[T.{arm}]'
    if term in model_e1.params.index:
        rows_e1.append({
            'arm_code': arm,
            'arm_label': arm_labels[arm],
            'estimate': round(model_e1.params[term], 4),
            'std_error': round(model_e1.bse[term], 4),
            'p_value': round(model_e1.pvalues[term], 4),
            'conf_low': round(model_e1.conf_int().loc[term, 0], 4),
            'conf_high': round(model_e1.conf_int().loc[term, 1], 4),
            'n_arm': int((df_e1['arm_code'] == arm).sum()),
            'n_control': int((df_e1['arm_code'] == 0).sum()),
        })

df_e1_results = pd.DataFrame(rows_e1)
df_e1_results.to_csv('results/E1_attention_check_robustness.csv', index=False)

# Figure: forest plot
fig, ax = plt.subplots(figsize=(8, 5))
y = np.arange(len(df_e1_results))[::-1]
ax.hlines(y,
          df_e1_results['conf_low'].values,
          df_e1_results['conf_high'].values,
          color=INK, alpha=0.5, linewidth=1.2)
ax.scatter(df_e1_results['estimate'].values, y, color=ACCENT, s=28, zorder=5)
ax.axvline(0, color=INK, linewidth=0.7, linestyle='--')
ax.set_yticks(y)
ax.set_yticklabels(df_e1_results['arm_label'].values, fontsize=9)
ax.set_xlabel('ATE on total_score (95% CI)', fontsize=10)
ax.set_title('E1: Total-Score Effects Excluding Attention-Check Failures\n'
             f'(n={len(df_e1)}, excluded {n_excluded} with pk_score=0)', fontsize=10)
for sp in ['top', 'right', 'left']:
    ax.spines[sp].set_visible(False)
ax.tick_params(left=False)
ax.grid(False)
plt.tight_layout()
plt.savefig('figures/E1_attention_check_robustness.png', dpi=200, facecolor='white')
plt.close()

sig_e1 = df_e1_results[df_e1_results['p_value'] < 0.05]
print(f"E1: Excluded {n_excluded} respondents (pk_score=0); n={len(df_e1)} remain. "
      f"{len(sig_e1)} arm(s) significant at p<.05: "
      f"{', '.join(f'{r.arm_label} ({r.estimate:+.3f})' for r in sig_e1.itertuples())}")

# ── E2: Age heterogeneity for AI Literacy Guide (arm 10) ──────────────────────
# Rationale: The AI Literacy Guide showed the largest positive effect on total_score
# (H1: +0.047, p=.043); testing whether this is concentrated in younger vs. older
# respondents informs whether the intervention works through age-specific channels.
print("\n" + "=" * 60)
print("E2: Age heterogeneity — AI Literacy Guide (arm 10) on total_score")
print("=" * 60)

df_e2 = df[df['age'].notna()].copy()
df_e2['age_group'] = np.where(df_e2['age'] < 40, 'Young (<40)', 'Older (>=40)')

formula_e2 = 'total_score ~ C(arm_code, Treatment(reference=0))'
term_10 = "C(arm_code, Treatment(reference=0))[T.10]"

rows_e2 = []
for grp in ['Young (<40)', 'Older (>=40)']:
    sub = df_e2[df_e2['age_group'] == grp]
    m = smf.wls(formula_e2, data=sub, weights=sub['ipw']).fit(cov_type='HC2')
    if term_10 in m.params.index:
        ci = m.conf_int().loc[term_10]
        rows_e2.append({
            'age_group': grp,
            'estimate': round(m.params[term_10], 4),
            'std_error': round(m.bse[term_10], 4),
            'p_value': round(m.pvalues[term_10], 4),
            'conf_low': round(ci[0], 4),
            'conf_high': round(ci[1], 4),
            'n_treated': int((sub['arm_code'] == 10).sum()),
            'n_control': int((sub['arm_code'] == 0).sum()),
        })

df_e2_results = pd.DataFrame(rows_e2)
df_e2_results.to_csv('results/E2_age_heterogeneity_arm10.csv', index=False)

# Figure: two-point comparison
fig, ax = plt.subplots(figsize=(5, 3.5))
x = [0, 1]
ests = df_e2_results['estimate'].values
ses = df_e2_results['std_error'].values
labs = df_e2_results['age_group'].values

ax.errorbar(x, ests, yerr=1.96 * ses, fmt='o', color=ACCENT,
            capsize=6, linewidth=1.5, markersize=9, ecolor=INK, elinewidth=1.2)
ax.axhline(0, color=INK, linewidth=0.7, linestyle='--')
ax.set_xticks(x)
ax.set_xticklabels(labs, fontsize=10)
ax.set_ylabel('ATE on total_score', fontsize=10)
ax.set_title('E2: AI Literacy Guide Effect by Age', fontsize=11)
for sp in ['top', 'right', 'left']:
    ax.spines[sp].set_visible(False)
ax.tick_params(left=False)
ax.grid(False)
for i in range(len(ests)):
    ax.annotate(f'{ests[i]:+.3f}', (x[i], ests[i] + 1.96 * ses[i] + 0.008),
                ha='center', fontsize=9, color=INK)
plt.tight_layout()
plt.savefig('figures/E2_age_heterogeneity_arm10.png', dpi=200, facecolor='white')
plt.close()

e2y = df_e2_results.iloc[0]
e2o = df_e2_results.iloc[1]
print(f"E2: AI Literacy Guide (arm 10) on total_score — "
      f"Young (<40): {e2y['estimate']:+.3f} (p={e2y['p_value']:.3f}, n={e2y['n_treated']}); "
      f"Older (>=40): {e2o['estimate']:+.3f} (p={e2o['p_value']:.3f}, n={e2o['n_treated']})")

# ── E3: Manipulation check — effect of arms on attention (pk_score) ───────────
# Rationale: If an intervention changes general attention (pk_score), it could
# explain outcome effects through a non-specific attention channel rather than
# the intended AI-detection mechanism.
print("\n" + "=" * 60)
print("E3: Manipulation check — arm effects on pk_score (attention)")
print("=" * 60)

formula_e3 = 'pk_score ~ C(arm_code, Treatment(reference=0))'
model_e3 = smf.wls(formula_e3, data=df, weights=df['ipw']).fit(cov_type='HC2')

rows_e3 = []
for arm in range(1, 12):
    term = f'C(arm_code, Treatment(reference=0))[T.{arm}]'
    if term in model_e3.params.index:
        ci = model_e3.conf_int().loc[term]
        rows_e3.append({
            'arm_code': arm,
            'arm_label': arm_labels[arm],
            'estimate': round(model_e3.params[term], 4),
            'std_error': round(model_e3.bse[term], 4),
            'p_value': round(model_e3.pvalues[term], 4),
            'conf_low': round(ci[0], 4),
            'conf_high': round(ci[1], 4),
            'n_arm': int((df['arm_code'] == arm).sum()),
        })

df_e3_results = pd.DataFrame(rows_e3)
df_e3_results.to_csv('results/E3_manipulation_check_attention.csv', index=False)

sig_e3 = df_e3_results[df_e3_results['p_value'] < 0.05]
max_idx = df_e3_results['estimate'].abs().idxmax()
max_arm = df_e3_results.loc[max_idx, 'arm_label']
max_est = df_e3_results.loc[max_idx, 'estimate']
print(f"E3: {len(sig_e3)} of 11 arms significantly change pk_score (p<.05). "
      f"Largest |effect|: {max_arm} ({max_est:+.3f}). "
      f"Mean pk_score (control) = {df.loc[df['arm_code']==0, 'pk_score'].mean():.3f}")

print("\nDone. All exploratory analyses complete.")
