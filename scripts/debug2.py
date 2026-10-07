"""Inspect the registered script's HYPOTHESES and build_formula."""
import importlib.util, pathlib
import pandas as pd

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

print("HYPOTHESES:")
for h in reg.HYPOTHESES:
    print(f"  {h}")
    print()

# Check what build_formula does with different inputs
df = pd.read_csv('data/clean.csv', nrows=5)
df['arm_code'] = pd.to_numeric(df['arm_code'], errors='coerce')
df['treat'] = pd.to_numeric(df['treat'], errors='coerce')
df['total_score'] = pd.to_numeric(df['total_score'], errors='coerce')
df['ipw'] = pd.to_numeric(df['ipw'], errors='coerce')

# Try with arm_code as estimator
print("\n--- build_formula with 'arm_code' as estimator ---")
try:
    f, d = reg.build_formula('total_score', 'arm_code', [], df)
    print("Formula:", f)
except Exception as e:
    print("Error:", e)

# Try with 'treat'
print("\n--- build_formula with 'treat' as estimator ---")
try:
    f, d = reg.build_formula('total_score', 'treat', [], df)
    print("Formula:", f)
except Exception as e:
    print("Error:", e)

# Check if there's a function for arm-level
print("\n\nAvailable functions in reg module:")
for name in dir(reg):
    if not name.startswith('_'):
        obj = getattr(reg, name)
        if callable(obj):
            print(f"  {name} (function)")
        elif isinstance(obj, (list, dict)):
            print(f"  {name} ({type(obj).__name__})")
