"""Temporary: print build_formula + CATEGORICAL + full H1 formula string."""
import pathlib
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
src = (ROOT / "scripts" / "03_registered.py").read_text()
i = src.find("CATEGORICAL")
print(src[max(0, i - 200): i + 400])
j = src.find("def build_formula")
print(src[j: j + 1200])
k = src.find("def fit")
print(src[k: k + 700])
df = pd.read_csv(ROOT / "results" / "registered_summary.csv")
print("FULL FORMULA H1:", df.loc[df["analysis_id"] == "H1:1", "formula"].iloc[0])
print("COV TYPE:", df.loc[df["analysis_id"] == "H1:1", "cov_type"].iloc[0])
