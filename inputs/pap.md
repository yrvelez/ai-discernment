# Analysis plan: Improving AI Discernment

**Registration status: none.** This study was not pre-registered. The plan below is a transcription of the
authors' analysis script (`code/replication_script.R`), so that the automated pipeline estimates exactly what the
script estimates. The structured version the pipeline runs is `inputs/pap.json`.

## Design

Randomized survey experiment, 12 arms: control plus 11 interventions drawn from the misinformation literature.
The arm is in the `treatment` column (0 = Control, 1 Flagging, 2 Provenance, 3 Automated Flagging,
4 AI Accuracy Nudge, 5 Breathing Exercise, 6 Mindfulness, 7 Inoculation, 8 AI Literacy Infographic,
9 AI Literacy Infographic 2, 10 AI Literacy Guide, 11 AI Text Video). Respondents then rated real and
AI-generated images and videos on a simulated social feed.

Assignment probabilities varied across fielding batches (column `pr`, the probability that a respondent was
assigned to their arm). All models are weighted by the inverse assignment probability, `ipw = 1 / pr`.

## Outcomes

- Primary: `total_score`, the share of all items classified correctly (0-1).
- Secondary: `fake_score` (share of AI-generated items classified correctly) and `real_score` (share of real
  items classified correctly).

Do not substitute any confidence or trust rating for these accuracy scores.

## Estimation

For each outcome, one model with all 11 arms against control, covariate adjustment following Lin (2013)
(covariates centred and fully interacted with the arm indicators), weights `1 / pr`, HC2 robust standard errors.
Covariates, all entering linearly: `media_trust`, `political_interest`, `pk_score`, and `ai_scale`, where
`ai_scale` is the share of seven AI tools the respondent uses:
`(chatgpt + bing + claude + character + dalle + midjourney + stable_diff) / 7`.

One row per respondent, so no clustering. Tests are two-sided at alpha = 0.05.

**No multiple-testing correction is applied, by design.** The script reports raw p-values for each arm; this
plan does the same.

A random-effects pooled estimate across the 11 arm effects is reported as a summary (the script uses REML via
`metafor::rma`; the pipeline uses an iterated random-effects estimator). The arm effects share one control group,
so the pooled standard error is approximate.

No sample exclusions beyond non-missing `treatment` and outcome.
