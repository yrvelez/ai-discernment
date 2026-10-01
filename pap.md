# Analysis plan: Improving AI Discernment

> **Not pre-registered.** This plan was reconstructed after data collection from the
> analysis code (`original/code/replication_script.R`) and the study write-up
> (`original/site/index.html`). It documents what the original analysis did so that the
> pipeline can tag each test as *planned* (matching the original script) or *exploratory*.
> No test in this package should be read as a confirmatory, pre-registered test.

## Design

Online survey experiment, U.S. adults recruited through CloudResearch, fielded 30 October
to 21 November 2023 in five batches (Columbia University IRB AAAU9484). After consent,
political-knowledge and interest items, media-trust items and a checklist of AI tools used,
respondents were assigned by an external web service (adaptive randomization across batches)
to one of twelve arms recorded in the embedded data field `treatment`:

| code | arm | description |
|---|---|---|
| 0 | Control | No intervention; proceed directly to the discernment task |
| 1 | Flagging | Content flagged as potentially AI-generated |
| 2 | Provenance | Information about the content's source and origin |
| 3 | Automated Flagging | Machine-learning-based AI-detection labels shown on content |
| 4 | AI Accuracy Nudge | Interactive task: "Is this image AI-generated?" |
| 5 | Breathing Exercise | Box breathing to reduce emotional reactivity |
| 6 | Mindfulness | Short mindfulness exercise |
| 7 | Inoculation | Pre-exposure to manipulation techniques (prebunking) |
| 8 | AI Literacy Infographic | Visual guide to identifying AI content |
| 9 | AI Literacy Infographic 2 | Alternative visual guide design |
| 10 | AI Literacy Guide | Comprehensive guide with examples of AI artifacts |
| 11 | AI Text Video | Educational video about AI-generated text |

Assignment probabilities differed across arms and batches; each respondent's assignment
probability is stored in `pr`. Analyses weight by the inverse of that probability.

Respondents then scrolled a simulated social feed ("FutureFeed") containing 24 posts, 12
authentic news images or videos and 12 AI-generated images or videos (deepfake videos of
political figures, fabricated images, synthetic headlines), and judged each post as
AI-generated or authentic.

## Outcomes

- **Primary: `total_score`**, the proportion of the 24 posts judged correctly (0 to 1).
- **Secondary: `fake_score`**, the proportion of the 12 AI-generated posts correctly identified
  as AI-generated.
- **Secondary: `real_score`**, the proportion of the 12 authentic posts correctly identified as
  authentic.

The per-item columns (`*_real_*`, `*_fake_*`) are the item-level correctness indicators from
which the scores were computed.

## Hypotheses (as tested in the original analysis)

- **H1.** Each intervention (arms 1 to 11) changes total discernment accuracy (`total_score`)
  relative to control. Two-sided tests, one coefficient per arm from a single model.
- **H2.** Each intervention changes detection of AI-generated content (`fake_score`) relative to
  control.
- **H3.** Each intervention changes recognition of authentic content (`real_score`) relative to
  control.

The original analysis also pooled the eleven arm effects for each outcome with a random-effects
meta-analysis (REML) to summarize whether misinformation-style interventions improve
discernment on average. Report the pooled estimate with the caveat that the eleven effects share
one control group, so they are not independent.

## Estimation

Lin (2013) covariate-adjusted regression (`estimatr::lm_lin` in the original): the outcome is
regressed on arm indicators (control as reference) fully interacted with mean-centered
covariates, with inverse-probability weights `1/pr`. Covariates: `media_trust`,
`political_interest`, `pk_score` (political knowledge, 0 to 2 correct), and `ai_scale`, the
proportion of seven AI tools the respondent reports having used (`chatgpt`, `bing`, `claude`,
`character`, `dalle`, `midjourney`, `stable_diff`; each 0/1). Heteroskedasticity-robust standard
errors (HC2). Two-sided tests at alpha = 0.05; no multiple-testing correction was applied in
the original analysis.

The original script requested standard errors clustered by `participant_id`. The shipped
replication data has one row per respondent and no `participant_id` column, so clustering is
not possible and, with one observation per respondent, not needed; use HC2 robust standard
errors instead and record this as a deviation from the original code.

## Sample and exclusions

Respondents with a recorded treatment assignment and a non-missing `total_score` form the
analysis sample (N = 2,030 of 2,257 rows in the file; the 227 excluded rows have no assignment
or assignment probability). No other exclusions; the attention check was not used for
exclusion in the original analysis.

## Heterogeneity

None planned in the original analysis.

## Exploratory analyses in the original write-up

The write-up reports which arms are significant at p < 0.05 and marginal at p < 0.10, and
describes the mindfulness arm as a backfire effect. Treat any further subgroup or item-level
analyses as exploratory.
