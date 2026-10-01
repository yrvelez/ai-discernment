"""
Exploratory analyses for the AI Discernment survey experiment.
Three pre-specified exploratory analyses to interpret registered results.
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

arm_labels = {
    0: 'Control', 1: 'Flagging', 2: 'Provenance', 3: 'Automated Flagging',
    4: 'AI Accuracy Nudge', 5: 'Breathing Exercise', 6: 'Mindfulness',
    7: 'Inoculation', 8: 'AI Literacy Infographic', 9: 'AI Literacy Infographic 2',
    10: 'AI Literacy Guide', 11: 'AI Text Video'
}

# Arms with significant H1 (total_score) effects: 3 (Auto Flag), 6 (Mindfulness), 10 (AI Guide)
sig_arms = [3, 6, 10]

# ── Helper ─────────────────────────────────────────────────────────────────────
def fit_arm_effects(sub, outcome='total_score'):
    """Fit OLS with HC2 for all arms vs control; return dict of arm -> stats."""
    sub = sub.dropna(subset=[outcome])
    if sub['arm_code'].nunique() < 2:
        return {}
    model = smf.ols(f'{outcome} ~ C(arm_code, Treatment(reference=0))', data=sub).fit(cov_type='HC2')
    out = {}
    for arm in range(1, 12):
        term = f'C(arm_code, Treatment(reference=0))[T.{arm}]'
        if term in model.params.index:
            ci = model.conf_int().loc[term]
            out[arm] = {
                'estimate': model.params[term],
                'std_error': model.bse[term],
                'p_value': model.pvalues[term],
                'conf_low': ci.iloc[0],
                'conf_high': ci.iloc[1],
                'n': int(model.nobs)
            }
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# E1: Heterogeneity by political interest
# Rationale: Politically interested respondents may be more motivated to
# discern media, potentially amplifying or attenuating intervention effects.
# ═══════════════════════════════════════════════════════════════════════════════
df['pol_int_group'] = np.where(df['political_interest'] <= 3, 'Low', 'High')

rows_e1 = []
for group in ['Low', 'High']:
    sub = df[df['pol_int_group'] == group]
    effects = fit_arm_effects(sub)
    for arm in sig_arms:
        if arm in effects:
            e = effects[arm]
            rows_e1.append({
                'analysis_id': f'E1:{arm}:{group}',
                'arm_code': arm,
                'arm_label': arm_labels[arm],
                'pol_int_group': group,
                'estimate': e['estimate'],
                'std_error': e['std_error'],
                'p_value': e['p_value'],
                'conf_low': e['conf_low'],
                'conf_high': e['conf_high'],
                'n': e['n']
            })

e1_df = pd.DataFrame(rows_e1)
e1_df.to_csv('results/E1_political_interest_heterogeneity.csv', index=False)

sig_e1 = e1_df[e1_df['p_value'] < 0.05]
af_low = e1_df[(e1_df.arm_code == 3) & (e1_df.pol_int_group == 'Low')]['estimate'].values
af_high = e1_df[(e1_df.arm_code == 3) & (e1_df.pol_int_group == 'High')]['estimate'].values
print(f"E1: Political interest heterogeneity — {len(sig_e1)}/{len(e1_df)} arm×group effects sig at p<.05; "
      f"Automated Flagging: Low={af_low[0]:+.3f}, High={af_high[0]:+.3f}")

# Figure E1
fig, ax = plt.subplots(figsize=(7.5, 3.8))
c_dark = '#2C3E50'
c_accent = '#C0392B'
y_pos = 0
ytick_labels = []
for arm in sig_arms:
    for group in ['Low', 'High']:
        row = e1_df[(e1_df.arm_code == arm) & (e1_df.pol_int_group == group)]
        if len(row):
            est, lo, hi = row['estimate'].values[0], row['conf_low'].values[0], row['conf_high'].values[0]
            col = c_dark if group == 'Low' else c_accent
            ax.errorbar(est, y_pos, xerr=[[est - lo], [hi - est]],
                        fmt='o', color=col, capsize=4, markersize=5, linewidth=1.2)
            ax.text(hi + 0.004, y_pos, f"{est:+.3f}", va='center', fontsize=8, color='#333')
            ytick_labels.append(f"{arm_labels[arm]} ({group})")
            y_pos += 1

ax.axvline(0, color='#999', linewidth=0.6, linestyle='--')
ax.set_yticks(range(y_pos))
ax.set_yticklabels(ytick_labels, fontsize=9)
ax.set_xlabel('Effect on total_score (95% CI)', fontsize=10)
ax.set_title('E1: H1-significant arms by political interest', fontsize=11, pad=10)
for sp in ['top', 'right', 'left']:
    ax.spines[sp].set_visible(False)
ax.grid(False)
plt.tight_layout()
plt.savefig('figures/E1_political_interest.png', dpi=200, bbox_inches='tight')
plt.close()

# ═══════════════════════════════════════════════════════════════════════════════
# E2: Robustness to attention-check failures
# Rationale: Excluding respondents who failed both attention checks (pk_score=0)
# tests whether registered effects are driven by inattentive respondents.
# ═══════════════════════════════════════════════════════════════════════════════
df_full = df.dropna(subset=['total_score'])
df_restricted = df[(df['pk_score'] > 0) & df['total_score'].notna()]

effects_full = fit_arm_effects(df_full)
effects_restricted = fit_arm_effects(df_restricted)

rows_e2 = []
for arm in range(1, 12):
    if arm in effects_full and arm in effects_restricted:
        ef, er = effects_full[arm], effects_restricted[arm]
        rows_e2.append({
            'analysis_id': f'E2:{arm}',
            'arm_code': arm,
            'arm_label': arm_labels[arm],
            'est_full': ef['estimate'], 'se_full': ef['std_error'], 'p_full': ef['p_value'],
            'ci_full_lo': ef['conf_low'], 'ci_full_hi': ef['conf_high'],
            'est_restricted': er['estimate'], 'se_restricted': er['std_error'], 'p_restricted': er['p_value'],
            'ci_restricted_lo': er['conf_low'], 'ci_restricted_hi': er['conf_high'],
            'n_full': ef['n'], 'n_restricted': er['n']
        })

e2_df = pd.DataFrame(rows_e2)
e2_df.to_csv('results/E2_attention_check_robustness.csv', index=False)

n_excluded = len(df_full) - len(df_restricted)
sig_f = e2_df[e2_df['p_full'] < 0.05]
sig_r = e2_df[e2_df['p_restricted'] < 0.05]
direction_match = all(
    np.sign(e2_df[e2_df.arm_code == a]['est_full'].values[0]) ==
    np.sign(e2_df[e2_df.arm_code == a]['est_restricted'].values[0])
    for a in sig_f['arm_code']
)
print(f"E2: Attention-check robustness — excluded {n_excluded} (pk_score=0); "
      f"{len(sig_f)} sig in full vs {len(sig_r)} in restricted; "
      f"direction preserved for all full-sample sig effects: {direction_match}")

# ═══════════════════════════════════════════════════════════════════════════════
# E3: Moderation by AI-tool familiarity (ai_scale)
# Rationale: Respondents already familiar with AI tools may have higher baseline
# detection skill, potentially attenuating the marginal benefit of interventions.
# ═══════════════════════════════════════════════════════════════════════════════
# Split: Low = ai_scale ≤ 0.286 (know ≤2 of 7 tools), High = > 0.286
df['ai_fam_group'] = np.where(df['ai_scale'] <= 0.286, 'Low', 'High')

rows_e3 = []
for group in ['Low', 'High']:
    sub = df[df['ai_fam_group'] == group]
    effects = fit_arm_effects(sub)
    for arm in sig_arms:
        if arm in effects:
            e = effects[arm]
            rows_e3.append({
                'analysis_id': f'E3:{arm}:{group}',
                'arm_code': arm,
                'arm_label': arm_labels[arm],
                'ai_fam_group': group,
                'estimate': e['estimate'],
                'std_error': e['std_error'],
                'p_value': e['p_value'],
                'conf_low': e['conf_low'],
                'conf_high': e['conf_high'],
                'n': e['n']
            })

e3_df = pd.DataFrame(rows_e3)
e3_df.to_csv('results/E3_ai_familiarity_moderation.csv', index=False)

sig_e3 = e3_df[e3_df['p_value'] < 0.05]
af3_low = e3_df[(e3_df.arm_code == 3) & (e3_df.ai_fam_group == 'Low')]['estimate'].values
af3_high = e3_df[(e3_df.arm_code == 3) & (e3_df.ai_fam_group == 'High')]['estimate'].values
print(f"E3: AI familiarity moderation — {len(sig_e3)}/{len(e3_df)} arm×group effects sig at p<.05; "
      f"Automated Flagging: Low-fam={af3_low[0]:+.3f}, High-fam={af3_high[0]:+.3f}")

# Figure E3
fig, ax = plt.subplots(figsize=(7.5, 3.8))
y_pos = 0
ytick_labels = []
for arm in sig_arms:
    for group in ['Low', 'High']:
        row = e3_df[(e3_df.arm_code == arm) & (e3_df.ai_fam_group == group)]
        if len(row):
            est, lo, hi = row['estimate'].values[0], row['conf_low'].values[0], row['conf_high'].values[0]
            col = c_dark if group == 'Low' else c_accent
            ax.errorbar(est, y_pos, xerr=[[est - lo], [hi - est]],
                        fmt='o', color=col, capsize=4, markersize=5, linewidth=1.2)
            ax.text(hi + 0.004, y_pos, f"{est:+.3f}", va='center', fontsize=8, color='#333')
            ytick_labels.append(f"{arm_labels[arm]} ({group})")
            y_pos += 1

ax.axvline(0, color='#999', linewidth=0.6, linestyle='--')
ax.set_yticks(range(y_pos))
ax.set_yticklabels(ytick_labels, fontsize=9)
ax.set_xlabel('Effect on total_score (95% CI)', fontsize=10)
ax.set_title('E3: H1-significant arms by AI-tool familiarity', fontsize=11, pad=10)
for sp in ['top', 'right', 'left']:
    ax.spines[sp].set_visible(False)
ax.grid(False)
plt.tight_layout()
plt.savefig('figures/E3_ai_familiarity.png', dpi=200, bbox_inches='tight')
plt.close()

print("All exploratory analyses complete.")
