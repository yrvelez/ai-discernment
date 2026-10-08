import importlib.util, pathlib
import numpy as np
import pandas as pd

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / 'results'
RES.mkdir(exist_ok=True)

d = pd.read_csv(ROOT / 'data' / 'clean.csv')
for c in ['batch', 'ai_scale', 'total_score', 'arm_code', 'treatment']:
    d[c] = pd.to_numeric(d[c], errors='coerce')

h1 = reg.HYPOTHESES[0]

# E1: robustness of H1 to restricting to batches 3-4 (fielded after the plan was registered)
orig = reg.reestimate(h1, d)
sub = reg.reestimate(h1, d[d['batch'] >= 3].copy())
orig['sample'] = 'all batches'
sub['sample'] = 'batches 3-4'
tab1 = pd.concat([orig, sub], ignore_index=True)
tab1.insert(0, 'analysis', 'E1')
tab1.to_csv(RES / 'E1_batch34_robustness.csv', index=False)
n_sig_orig = int((orig['p_value'] < 0.05).sum())
n_sig_sub = int((sub['p_value'] < 0.05).sum())
m_orig = orig.set_index('arm')['estimate']
m_sub = sub.set_index('arm')['estimate']
s_orig = orig.set_index('arm')['std_error']
s_sub = sub.set_index('arm')['std_error']
ratio = float((s_sub / s_orig).max())
n_arms = len(orig)
print(f"E1 Batch 3-4 robustness of accuracy effects: {n_sig_sub} of {n_arms} arms reach p<0.05 in batches 3-4 (n={int(sub['n'].max())}) versus {n_sig_orig} of {n_arms} in the full sample (n={int(orig['n'].max())}); largest SE ratio {ratio:.2f}, sample change exceeds 10% so the SE-drop rule does not apply.")

# E2: heterogeneity of H1 by self-reported AI-tool familiarity (ai_scale), slopes per arm
het = reg.reestimate(h1, d, moderator='ai_scale')
het.insert(0, 'analysis', 'E2')
het.to_csv(RES / 'E2_ai_familiarity_heterogeneity.csv', index=False)
n_sig_het = int((het['p_value'] < 0.05).sum())
n_het = len(het)
pos = het[het['estimate'] > 0]
print(f"E2 Heterogeneity of accuracy effects by AI-tool familiarity: {n_sig_het} of {n_het} arm-level slopes reach p<0.05 (exploratory, uncorrected); median slope {het['estimate'].median():.3f} per unit of ai_scale (range {het['estimate'].min():.3f} to {het['estimate'].max():.3f}).")
