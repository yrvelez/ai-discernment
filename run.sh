#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY (bring your own token)}"
filedrawer run --csv inputs/export.csv --qsf inputs/survey.qsf --pap inputs/pap.md \
  --slug "ai-discernment" --title "Improving AI Discernment" --authors "Yamil R. Velez" --repo-url "https://github.com/yrvelez/ai-discernment" \
  --package-dir . --pap-json inputs/pap.json --no-silicon --review "$@"
