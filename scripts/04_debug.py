import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

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

num_cols = ['total_score', 'pk_score', 'political_interest', 'fake_score', 'real_score',
            'ai_attitudes', 'ai_confidence', 'trust_online', 'media_trust', 'age',
            'gender_m', 'white', 'hisp', 'afam_black', 'asian', 'ipw', 'treat', 'ai_scale']
for c in num_cols:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

h1 = [h for h in reg.HYPOTHESES if h.get('outcome') == 'total_score'][0]
est = h1['estimator']
covariates = est['covariates']

# Quick debug: see what params look like
df_full = df.dropna(subset=['total_score']).copy()
f_orig, d_orig = reg.build_formula('total_score', est, covariates, df_full)
res_orig = reg.fit(d_orig, f_orig, est)
print(f"[debug] formula: {f_orig}")
print(f"[debug] params index: {list(res_orig.params.index[:20])}")
print(f"[debug] d_orig columns: {list(d_orig.columns[:15])}")
