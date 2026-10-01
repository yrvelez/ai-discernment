#!/usr/bin/env bash
# Runs the filedrawer pipeline on this study. Needs: pip install "filedrawer @ git+https://github.com/yrvelez/filedrawer"
set -euo pipefail
cd "$(dirname "$0")"
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY (bring your own token)}"
filedrawer run \
  --csv inputs/replication_data.csv --qsf inputs/survey.qsf --pap inputs/pap.md --pap-json inputs/pap.json \
  --arm-column treatment \
  --slug ai-discernment --title "Improving AI Discernment: do misinformation interventions help people spot AI-generated media?" \
  --authors "Yamil Velez" --repo-url https://github.com/yrvelez/ai-discernment \
  --package-dir . --review "$@"
