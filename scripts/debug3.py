"""Inspect the registered script source - full."""
import pathlib
src = pathlib.Path('scripts/03_registered.py').read_text()
# Print in chunks
print("=== LINES 1-80 ===")
for i, line in enumerate(src.split('\n')[:80], 1):
    print(f"{i:3d}: {line}")
