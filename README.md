# Improving AI Discernment

Replication package for a survey experiment testing whether interventions from the misinformation
literature improve people's ability to tell AI-generated images and videos from authentic news media.
Twelve treatment arms (including flagging, provenance, inoculation, accuracy nudges, mindfulness and
AI-literacy training) were compared to control on a simulated social feed ("FutureFeed").

Columbia University. IRB protocol AAAU9484.

## Contents

| Path | What it is |
|---|---|
| `data/replication_data.csv` | De-identified analysis data, one row per respondent |
| `code/replication_script.R` | Runs the analysis from `replication_data.csv` |
| `code/create_replication_data.R` | Builds the replication data from the raw Qualtrics export (expects the raw export in `raw_data/`, not included) |
| `materials/Improving_AI_Discernment.qsf` | Qualtrics survey instrument (import into Qualtrics) |
| `site/index.html` | Standalone write-up of the study and results |

## Reproducing

From the repository root:

```bash
Rscript code/replication_script.R
```

Requires R with `tidyverse`, `estimatr`, `broom` and `metafor`.

## Data and privacy

The raw Qualtrics export (IP addresses, coordinates, worker IDs) is not in this repo. IP, location,
recipient and worker identifiers were removed and participant IDs pseudonymized in
`create_replication_data.R`. `.gitignore` blocks the raw export.

Treatment labels: 0 Control, 1 Flagging, 2 Provenance, 3 Automated Flagging, 4 AI Accuracy Nudge,
5 Breathing Exercise, 6 Mindfulness, 7 Inoculation, 8 AI Literacy Infographic,
9 AI Literacy Infographic 2, 10 AI Literacy Guide, 11 AI Text Video.
