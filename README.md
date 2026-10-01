# Improving AI Discernment

Survey experiment testing whether interventions from the misinformation literature improve people's
ability to tell AI-generated images and videos from authentic news media. Twelve arms (control plus
flagging, provenance, automated flagging, accuracy nudge, breathing, mindfulness, inoculation, three
AI-literacy materials and an AI-text video) on a simulated social feed ("FutureFeed"); U.S. adults via
CloudResearch, fielded 30 October to 21 November 2023; N = 2,030 analyzed. Columbia University IRB AAAU9484.

This repository is a study package in the [filedrawer](https://github.com/yrvelez/filedrawer) layout.
**It is not pre-registered**: the analysis plan in `inputs/pap.md` was reconstructed after the fact from
the original analysis script, so the pipeline labels every test *planned, not pre-registered* or
*exploratory*. The package at the root of the repository (report, tidy data, scripts, results,
provenance) is produced by `./run.sh`; nothing in it is hand-edited.

## Layout

| Path | What it is |
|---|---|
| `inputs/replication_data.csv` | De-identified analysis data, one row per respondent (2,257 rows; 2,030 with an assignment) |
| `inputs/survey.qsf` | Qualtrics survey instrument (schema only, no responses) |
| `inputs/pap.md` | Analysis plan, reconstructed post hoc (read this first) |
| `inputs/pap.json` | The same plan, structured for the pipeline (arms, outcomes, estimator, deviations) |
| `original/code/` | The original R analysis (`replication_script.R`, Lin estimator with IPW) and the de-identification script |
| `original/site/` | The original standalone HTML write-up |
| `run.sh` | Runs the pipeline with your own OpenRouter key |
| `report.md`, `study.json`, `data/`, `scripts/`, `results/`, `figures/`, `silicon/`, `provenance/` | Generated package (appear after `./run.sh`) |

## Reproduce

```bash
pip install "filedrawer @ git+https://github.com/yrvelez/filedrawer"
export OPENROUTER_API_KEY=sk-or-...
./run.sh                 # writes the package at the repo root; add --no-silicon or --no-lit to skip extensions
filedrawer reproduce .   # re-runs the generated scripts and checks every results table is byte-identical
```

The original R analysis: `Rscript original/code/replication_script.R` (needs tidyverse, estimatr, broom,
metafor). Note that it clusters standard errors by `participant_id`, a column the de-identified data
does not contain; the pipeline uses HC2 robust standard errors instead and records that as a deviation.

## Data and privacy

The raw Qualtrics export (IP addresses, coordinates, worker IDs) is not in this repository and is
gitignored. `original/code/create_replication_data.R` documents the de-identification. The pipeline's
own PII scan runs again on `inputs/replication_data.csv` and drops anything identifier-like
(`StartDate` is removed; `batch` is kept).

## Citing and filing

File this repository on the File Drawer journal by pasting its URL on the Submit page; the journal
reads `study.json` and `report.md` and links back here. Data and code: CC BY 4.0 unless noted.
