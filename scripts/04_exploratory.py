"""
Exploratory analyses for the AI Discernment survey experiment.
Three analyses:
  E1: Heterogeneity by prior AI familiarity (ChatGPT user vs non-user)
  E2: False-alarm trade-off across AI-literacy arms
  E3: Robustness excluding attention-check failures (pk_score = 0)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('results', exist_ok=True)
os.makedirs('figures', exist_ok=True)

df = pd.read_csv('data/clean.csv')

# ── Figure style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'xtick.color': '#333333',
    'ytick.color': '#333333',
    'text.color': '#333333',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'font.size': 10,
})
ACCENT = '#2171b5'
INK = '#333333'
GREY = '#999999'

# ══════════════════════════════════════════════════════════════════════════════
# E1: Heterogeneity by prior AI familiarity (ChatGPT user)
# Rationale: AI-literacy interventions may have differential effects depending
# on whether respondents already use AI tools; this interaction helps interpret
# whether the significant H1 effects are driven by a specific subgroup.
# ══════════════════════════════════════════════════════════════════════════════
df['chatgpt_bin'] = (df['chatgpt'] == 1).astype(int)
sig_arms = [3, 6, 10]
arm_labels = {3: 'Automated Flagging', 6: 'Mindfulness', 10: 'AI Literacy Guide'}

df_e1 = df[df['arm_code'].isin([0] + sig_arms)].copy()
formula_e1 = 'total_score ~ C(arm_code, Treatment(reference=0)) * C(chatgpt_bin)'
model_e1 = smf.ols(formula_e1, data=df_e1).fit(weights=df_e1['ipw'], cov_type='HC2')

rows_e1 = []
for arm in sig_arms:
    term_main = f"C(arm_code, Treatment(reference=0))[T.{arm}]"
    term_int = f"C(arm_code, Treatment(reference=0))[T.{arm}]:C(chatgpt_bin)[T.1]"

    est_main = model_e1.params[term_main]
    se_main = model_e1.bse[term_main]
    p_main = model_e1.pvalues[term_main]

    est_int = model_e1.params[term_int]
    se_int = model_e1.bse[term_int]
    p_int = model_e1.pvalues[term_int]

    # Treatment effect for ChatGPT users = main + interaction
    est_users = est_main + est_int
    cov_mat = model_e1.cov_params()
    se_users = np.sqrt(se_main**2 + se_int**2 + 2 * cov_mat.loc[term_main, term_int])
    p_users = 2 * (1 - stats.norm.cdf(abs(est_users / se_users)))

    rows_e1.append({'arm_code': arm, 'arm_label': arm_labels[arm], 'group': 'Non-users',
                    'estimate': est_main, 'std_error': se_main, 'p_value': p_main,
                    'conf_low': est_main - 1.96 * se_main, 'conf_high': est_main + 1.96 * se_main})
    rows_e1.append({'arm_code': arm, 'arm_label': arm_labels[arm], 'group': 'ChatGPT users',
                    'estimate': est_users, 'std_error': se_users, 'p_value': p_users,
                    'conf_low': est_users - 1.96 * se_users, 'conf_high': est_users + 1.96 * se_users})
    rows_e1.append({'arm_code': arm, 'arm_label': arm_labels[arm], 'group': 'Interaction',
                    'estimate': est_int, 'std_error': se_int, 'p_value': p_int,
                    'conf_low': est_int - 1.96 * se_int, 'conf_high': est_int + 1.96 * se_int})

df_e1_out = pd.DataFrame(rows_e1)
df_e1_out.to_csv('results/E1_heterogeneity_chatgpt.csv', index=False)

# Figure: forest plot (non-users vs users for each arm)
plot_df = df_e1_out[df_e1_out['group'].isin(['Non-users', 'ChatGPT users'])].reset_index(drop=True)
fig, ax = plt.subplots(figsize=(7, 3.5))
for i, row in plot_df.iterrows():
    color = ACCENT if row['group'] == 'ChatGPT users' else INK
    ax.plot([row['conf_low'], row['conf_high']], [i, i], color=color, lw=1.5, zorder=2, solid_capstyle='round')
    ax.plot(row['estimate'], i, 'o', color=color, ms=7, zorder=3)
    ax.annotate(f"{row['estimate']:+.3f}", (row['conf_high'], i),
                textcoords='offset points', xytext=(5, 0), fontsize=8, va='center', color=color)

ax.axvline(0, color=GREY, lw=0.8, ls='--')
ax.set_yticks(range(len(plot_df)))
ax.set_yticklabels([f"{r['arm_label']}  ({r['group']})" for _, r in plot_df.iterrows()], fontsize=9)
ax.set_xlabel('Effect on total discernment accuracy (vs control)')
ax.set_title('E1: Treatment effects by prior AI familiarity', fontsize=11, loc='left', pad=10)
plt.tight_layout()
plt.savefig('figures/E1_heterogeneity_chatgpt.png', dpi=200)
plt.close()

int_ps = {a: model_e1.pvalues[f"C(arm_code, Treatment(reference=0))[T.{a}]:C(chatgpt_bin)[T.1]"] for a in sig_arms}
print(f"E1: ChatGPT-use interaction p-values — " +
      ", ".join([f"{arm_labels[a]}: p={int_ps[a]:.3f}" for a in sig_arms]) +
      f"  (no significant heterogeneity)" if max(int_ps.values()) > 0.10 else
      f"E1: ChatGPT-use interaction — significant for " +
      ", ".join([arm_labels[a] for a in sig_arms if int_ps[a] < 0.10]))

# ══════════════════════════════════════════════════════════════════════════════
# E2: False-alarm trade-off across AI-literacy arms
# Rationale: The registered H3 found a significant negative effect of AI Literacy
# Infographic 2 on real_score; examining whether this "false alarm" pattern is
# shared across all AI-literacy arms (8–11) clarifies whether it is a general
# cost of AI-literacy training.
# ══════════════════════════════════════════════════════════════════════════════
lit_arms = [8, 9, 10, 11]
lit_labels = {8: 'AI Literacy Infographic', 9: 'AI Literacy Infographic 2',
              10: 'AI Literacy Guide', 11: 'AI Text Video'}

df_e2 = df[df['arm_code'].isin([0] + lit_arms)].copy()

rows_e2 = []
for arm in lit_arms:
    for outcome in ['fake_score', 'real_score']:
        m = smf.ols(f'{outcome} ~ C(arm_code, Treatment(reference=0))', data=df_e2).fit(
            weights=df_e2['ipw'], cov_type='HC2')
        term = f"C(arm_code, Treatment(reference=0))[T.{arm}]"
        est, se, p = m.params[term], m.bse[term], m.pvalues[term]
        rows_e2.append({'arm_code': arm, 'arm_label': lit_labels[arm], 'outcome': outcome,
                        'estimate': est, 'std_error': se, 'p_value': p,
                        'conf_low': est - 1.96 * se, 'conf_high': est + 1.96 * se})

df_e2_out = pd.DataFrame(rows_e2)
df_e2_out.to_csv('results/E2_false_alarm_tradeoff.csv', index=False)

# Figure: scatter of Δfake vs Δreal with CIs
fig, ax = plt.subplots(figsize=(6, 5))
for arm in lit_arms:
    fr = df_e2_out[(df_e2_out['arm_code'] == arm) & (df_e2_out['outcome'] == 'fake_score')].iloc[0]
    rr = df_e2_out[(df_e2_out['arm_code'] == arm) & (df_e2_out['outcome'] == 'real_score')].iloc[0]
    ax.errorbar(fr['estimate'], rr['estimate'],
                xerr=[[fr['estimate'] - fr['conf_low']], [fr['conf_high'] - fr['estimate']]],
                yerr=[[rr['estimate'] - rr['conf_low']], [rr['conf_high'] - rr['estimate']]],
                fmt='o', color=ACCENT, ms=9, capsize=4, elinewidth=1.2, zorder=3)
    ax.annotate(lit_labels[arm], (fr['estimate'], rr['estimate']),
                textcoords='offset points', xytext=(10, 6), fontsize=9)

ax.axhline(0, color=GREY, lw=0.8, ls='--')
ax.axvline(0, color=GREY, lw=0.8, ls='--')
ax.set_xlabel('Δ fake_score  (detection of AI-generated content)')
ax.set_ylabel('Δ real_score  (recognition of authentic content)')
ax.set_title('E2: Detection–recognition trade-off, AI-literacy arms', fontsize=11, loc='left', pad=10)
plt.tight_layout()
plt.savefig('figures/E2_false_alarm_tradeoff.png', dpi=200)
plt.close()

for arm in lit_arms:
    fr = df_e2_out[(df_e2_out['arm_code'] == arm) & (df_e2_out['outcome'] == 'fake_score')].iloc[0]
    rr = df_e2_out[(df_e2_out['arm_code'] == arm) & (df_e2_out['outcome'] == 'real_score')].iloc[0]
    print(f"E2: {lit_labels[arm]}: Δfake={fr['estimate']:+.3f} (p={fr['p_value']:.3f}), "
          f"Δreal={rr['estimate']:+.3f} (p={rr['p_value']:.3f})")

# ══════════════════════════════════════════════════════════════════════════════
# E3: Robustness excluding attention-check failures (pk_score = 0)
# Rationale: Respondents who fail both attention checks may not have engaged
# with the discernment task; excluding them tests whether the registered pooled
# effect is robust to this exclusion.
# ══════════════════════════════════════════════════════════════════════════════
n_excluded = (df['pk_score'] == 0).sum()
df_e3 = df[df['pk_score'] > 0].copy()

model_e3 = smf.ols('total_score ~ C(arm_code, Treatment(reference=0))', data=df_e3).fit(
    weights=df_e3['ipw'], cov_type='HC2')

rows_e3 = []
for arm in range(1, 12):
    term = f"C(arm_code, Treatment(reference=0))[T.{arm}]"
    est, se, p = model_e3.params[term], model_e3.bse[term], model_e3.pvalues[term]
    rows_e3.append({'arm_code': arm, 'estimate': est, 'std_error': se, 'p_value': p,
                    'conf_low': est - 1.96 * se, 'conf_high': est + 1.96 * se})

# Pooled: simple mean of arm-specific estimates with SE from their spread
ests = [model_e3.params[f"C(arm_code, Treatment(reference=0))[T.{a}]"] for a in range(1, 12)]
ses = [model_e3.bse[f"C(arm_code, Treatment(reference=0))[T.{a}]"] for a in range(1, 12)]
pooled_est = float(np.mean(ests))
pooled_se = float(np.std(ses, ddof=1) / np.sqrt(11))
pooled_p = float(2 * (1 - stats.norm.cdf(abs(pooled_est / pooled_se))))
rows_e3.append({'arm_code': 'pooled', 'estimate': pooled_est, 'std_error': pooled_se,
                'p_value': pooled_p, 'conf_low': pooled_est - 1.96 * pooled_se,
                'conf_high': pooled_est + 1.96 * pooled_se})

df_e3_out = pd.DataFrame(rows_e3)
df_e3_out.to_csv('results/E3_robustness_pk.csv', index=False)

print(f"E3: Excluding pk_score=0 (n_excluded={n_excluded}, n_remaining={len(df_e3)}): "
      f"pooled effect={pooled_est:+.4f} (SE={pooled_se:.4f}, p={pooled_p:.3f}) "
      f"vs registered 0.010 (p=0.132)")
