"""
Exploratory analyses for the AI Discernment survey experiment.
Three analyses:
  E1: Heterogeneity by prior AI experience (ChatGPT usage)
  E2: Item-level analysis of real-content recognition (false-alarm pattern)
  E3: Robustness to attention-check failures (pk_score = 0 exclusion)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('results', exist_ok=True)
os.makedirs('figures', exist_ok=True)

df = pd.read_csv('data/clean.csv')
df['arm_code'] = df['arm_code'].astype(str)
df['chatgpt'] = df['chatgpt'].astype(int)
df['ipw'] = 1.0 / df['pr']

# ============================================================
# E1: Heterogeneity by prior AI experience (ChatGPT usage)
# Rationale: AI-literacy interventions may work better for those
# with less prior AI experience; a pooled treatment × familiarity
# interaction tests whether effects are driven by knowledge gaps.
# ============================================================
df['treat_any'] = (df['arm_code'] != '0').astype(int)

formula_e1 = 'total_score ~ C(treat_any) * C(chatgpt)'
model_e1 = smf.wls(formula_e1, data=df, weights=df['ipw'])
res_e1 = model_e1.fit(cov_type='HC2')

interact_term = 'C(treat_any)[T.1]:C(chatgpt)[T.1]'
treat_term = 'C(treat_any)[T.1]'
chat_term = 'C(chatgpt)[T.1]'

e1_rows = []
for label, term in [
    ('Pooled treatment effect (any vs control)', treat_term),
    ('ChatGPT usage (main effect)', chat_term),
    ('Treatment x ChatGPT interaction', interact_term),
]:
    est = res_e1.params[term]
    se = res_e1.bse[term]
    p = res_e1.pvalues[term]
    e1_rows.append({
        'term': label,
        'estimate': round(est, 4),
        'std_error': round(se, 4),
        'p_value': round(p, 4),
        'ci_low': round(est - 1.96 * se, 4),
        'ci_high': round(est + 1.96 * se, 4),
    })

e1_df = pd.DataFrame(e1_rows)
e1_df.to_csv('results/E1_ai_familiarity_interaction.csv', index=False)

interact_est = res_e1.params[interact_term]
interact_se = res_e1.bse[interact_term]
interact_p = res_e1.pvalues[interact_term]
print(f"E1: Pooled treatment x ChatGPT interaction on total_score: "
      f"est={interact_est:.4f}, SE={interact_se:.4f}, p={interact_p:.4f}")

# ============================================================
# E2: Item-level analysis of real-content recognition
# Rationale: Several arms (Breathing, Infographic 2, Guide) show
# patterns suggesting increased false alarms on real content;
# item-level inspection reveals whether the effect is
# concentrated on particular content types.
# ============================================================
real_items = [
    'biden2_real_news_005.png', 'biden_real_005.png',
    'biden_real_news_001.png', 'election_real_news_006.png',
    'google_real_news_003.png', 'hot_weather_real_news_008.png',
    'jim_jordan_real_news_007.png', 'johnson_real_003.mp4',
    'poland_real_news_002.png', 'protest_real_news_004.png',
    'putin_real_002.webp', 'unhorse_real_004.png',
    'untrump_real_001.webp'
]

arms_of_interest = ['5', '9', '10']
arm_labels = {'5': 'Breathing Exercise', '9': 'AI Literacy Infographic 2',
              '10': 'AI Literacy Guide'}

e2_rows = []
for arm in arms_of_interest:
    ctrl = df[df['arm_code'] == '0']
    trt = df[df['arm_code'] == arm]
    for item in real_items:
        ctrl_mean = ctrl[item].mean()
        trt_mean = trt[item].mean()
        diff = trt_mean - ctrl_mean
        e2_rows.append({
            'arm_code': arm,
            'arm_label': arm_labels[arm],
            'item': item,
            'mean_control': round(ctrl_mean, 4),
            'mean_treated': round(trt_mean, 4),
            'diff': round(diff, 4),
            'n_control': int(ctrl[item].notna().sum()),
            'n_treated': int(trt[item].notna().sum()),
        })

e2_df = pd.DataFrame(e2_rows)
e2_df.to_csv('results/E2_real_item_analysis.csv', index=False)

e2_summary = e2_df.groupby(['arm_code', 'arm_label'])['diff'].mean().reset_index()
e2_summary.columns = ['arm_code', 'arm_label', 'mean_item_diff']
print("E2: Mean item-level diff on real content — " +
      ", ".join([f"{r.arm_label}: {r.mean_item_diff:.4f}"
                 for r in e2_summary.itertuples()]))

# Figure: horizontal bar charts, one panel per arm
fig, axes = plt.subplots(1, 3, figsize=(15, 6), sharey=True)
for ax, arm in zip(axes, arms_of_interest):
    sub = e2_df[e2_df['arm_code'] == arm].copy()
    short_labels = [x.replace('.png', '').replace('.mp4', '').replace('.webp', '')
                    for x in sub['item']]
    colors = ['#e74c3c' if d < 0 else '#27ae60' for d in sub['diff']]
    ax.barh(range(len(sub)), sub['diff'], color=colors, edgecolor='white', height=0.7)
    ax.set_yticks(range(len(sub)))
    ax.set_yticklabels(short_labels, fontsize=7)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_title(arm_labels[arm], fontsize=11, fontweight='bold')
    ax.set_xlabel('Diff from control (treated − control)')
    ax.set_xlim(-0.15, 0.15)
plt.suptitle('E2: Item-level accuracy on real content vs. control', y=1.02, fontsize=12)
plt.tight_layout()
plt.savefig('figures/E2_real_item_diffs.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================
# E3: Robustness — exclude attention-check failures (pk_score=0)
# Rationale: Respondents failing both attention checks may not
# have engaged with the task; excluding them tests whether the
# registered results are robust to this alternative exclusion.
# ============================================================
n_before = len(df)
df_e3 = df[df['pk_score'] > 0].copy()
n_excluded = n_before - len(df_e3)

formula_e3 = 'total_score ~ C(arm_code, Treatment(reference="0"))'
model_e3 = smf.wls(formula_e3, data=df_e3, weights=df_e3['ipw'])
res_e3 = model_e3.fit(cov_type='HC2')

e3_rows = []
for arm in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
    term = f'C(arm_code, Treatment(reference="0"))[T.{arm}]'
    if term in res_e3.params.index:
        est = res_e3.params[term]
        se = res_e3.bse[term]
        p = res_e3.pvalues[term]
        e3_rows.append({
            'arm_code': arm,
            'estimate': round(est, 4),
            'std_error': round(se, 4),
            'p_value': round(p, 4),
            'ci_low': round(est - 1.96 * se, 4),
            'ci_high': round(est + 1.96 * se, 4),
        })

e3_df = pd.DataFrame(e3_rows)
e3_df.to_csv('results/E3_no_attention_failures.csv', index=False)

sig_arms = {'3': 'Automated Flagging', '6': 'Mindfulness', '10': 'AI Literacy Guide'}
sig_results = e3_df[e3_df['arm_code'].isin(sig_arms.keys())]
print(f"E3: N={len(df_e3)} (excluded {n_excluded} with pk_score=0). "
      f"Previously significant arms: " +
      ", ".join([f"{sig_arms[r.arm_code]}: est={r.estimate:.4f}, p={r.p_value:.4f}"
                 for r in sig_results.itertuples()]))

print("\nAll exploratory analyses complete.")
