"""Debug: check formula and parameter names."""
import importlib.util, pathlib
import numpy as np
import pandas as pd
import re

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

df = pd.read_csv('data/clean.csv')
for col in ['total_score', 'political_interest', 'ai_scale', 'ipw', 'arm_code', 'pk_score']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

h1 = next(h for h in reg.HYPOTHESES if h['outcome'] == 'total_score')
est_h1 = h1['estimator']
covariates_h1 = h1.get('covariates', [])

print("Covariates:", covariates_h1)

# Build the base formula
formula, d = reg.build_formula('total_score', est_h1, covariates_h1, df)
print("\nBase formula:", formula)
print("\nFirst 20 param names from base fit:")
res = reg.fit(d, formula, est_h1)
for name in res.params.index[:20]:
    print(f"  {name}")

# Now try adding pi_c
d1 = df.dropna(subset=['total_score', 'political_interest']).copy()
d1['pi_c'] = d1['political_interest'] - d1['political_interest'].mean()

formula_e1, d1b = reg.build_formula('total_score', est_h1, covariates_h1, d1)
print("\n\nFormula with pi_c in data (no formula change):", formula_e1)

# Manually modify
lhs, rhs = formula_e1.split('~')
rhs = rhs.strip()
print("\nRHS:", rhs)

arm_pattern = r"C\(arm_code, Treatment\(reference='0'\)\)"
m = re.search(arm_pattern, rhs)
print("\nArm match:", m)
if m:
    print("Arm string:", m.group(0))
    after_arm = rhs[m.end():]
    print("After arm:", after_arm[:100])
    if after_arm.strip().startswith('*'):
        paren_start = after_arm.index('(')
        paren_end = after_arm.index(')', paren_start)
        inner = after_arm[paren_start+1:paren_end].strip()
        print("Inner:", inner)
        new_inner = f"pi_c + {inner}"
        new_rhs = rhs[:m.start()] + m.group(0) + after_arm[:paren_start+1] + new_inner + after_arm[paren_end:]
        print("\nNew RHS:", new_rhs[:200])
        formula_new = f"{lhs.strip()} ~ {new_rhs}"
        print("\nNew formula:", formula_new[:300])
        res_new = reg.fit(d1b, formula_new, est_h1)
        print("\nParam names with pi_c interaction:")
        for name in res_new.params.index:
            if 'pi_c' in str(name):
                print(f"  {name}: {res_new.params[name]:.4f}")
