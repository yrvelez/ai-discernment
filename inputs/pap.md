# Pre-analysis plan: Improving AI Discernment

**Pre-registered.** AsPredicted #151,281, "AI Detection - Adaptive Experiment", registered 2023-11-15 12:54 PT,
https://aspredicted.org/q2eh95.pdf. It amends AsPredicted #151208 (the earlier version used a latent-trait
accuracy estimate; this version uses an overall accuracy score as the primary outcome). Data collection for
the first batch had begun and the second batch was in progress at registration; batches 3 and 4 followed
the registered plan.

The pre-registration text is transcribed verbatim in the next section. The section after it maps each
registered quantity to a column in `inputs/replication_data.csv`; every mapping choice is recorded as an
interpretation in `inputs/pap.json`.

## Pre-registration (verbatim)

1) Have any data been collected for this study already?
It's complicated. We have already collected some data but explain in Question 8 why readers may consider
this a valid pre-registration nevertheless.

2) What's the main question being asked or hypothesis being tested in this study?
What are the most effective methods for improving the accuracy of detecting generative AI?

3) Describe the key dependent variable(s) specifying how they will be measured.
Note: This pre-analysis plan amends #151208. To facilitate interpretability of the outcome, an overall
accuracy score, rather than a latent trait estimate, will be reported and used as the primary dependent
variable.
Accuracy: We will measure accuracy using 24 videos/images that vary in their use of Generative AI.
AI Attitudes: We will measure attitudes toward AI using a six-item scale capturing whether AI is seen as an
opportunity or threat.
Confidence in AI detection: We will measure confidence using a single 7-point Likert item capturing
confidence in ability to detect AI.
Trust in online information: We will measure (dis)trust in online information using a seven-item scale
capturing willingness to believe and verify information.

4) How many and which conditions will participants be assigned to?
There is one control condition and 11 experimental conditions, each corresponding to a student-submitted
intervention.

5) Specify exactly which analyses you will conduct to examine the main question/hypothesis.
Linear regression of each outcome on treatment indicators, media trust, political knowledge, AI usage, and
political interest using the Lin (2013) estimator.
Treatment assignment probabilities will be determined using an adaptive algorithm (Offer-Westort et al.
2021). Gaussian Thompson sampling will be implemented, with the objective of improving AI detection
accuracy. We will weigh observations using inverse probability weighting.

6) Describe exactly how outliers will be defined and handled, and your precise rule(s) for excluding
observations.
No exclusions

7) How many observations will be collected or what will determine sample size?
2,000

8) Anything else you would like to pre-register?
Data collection for the second batch is currently in progress. Treatment assignment probabilities in the
third batch will be based on the simpler outcome measure. No other changes are expected.

## Mapping to the data

Arms: column `treatment`; 0 = Control, 1 Flagging, 2 Provenance, 3 Automated Flagging, 4 AI Accuracy
Nudge, 5 Breathing Exercise, 6 Mindfulness, 7 Inoculation, 8 AI Literacy Infographic, 9 AI Literacy
Infographic 2, 10 AI Literacy Guide, 11 AI Text Video. Each arm is one student-submitted intervention.

Registered outcomes:

- Accuracy (primary): `total_score`, share of the 24 posts judged correctly (0 to 1).
- AI attitudes: mean of `ai_outcome_1` to `ai_outcome_6` (7-point agree scales). Items 4 ("a threat to
  humans") and 6 ("used to manipulate me") are reverse-coded so that higher values mean AI is seen as an
  opportunity. The registration does not state the scoring direction; this is an interpretation.
- Confidence in AI detection: `ai_outcome_7`, "I feel confident in my ability to detect artificial
  intelligence" (1 to 7).
- Trust in online information: mean of `trust_online_1` to `trust_online_7` (5-point agree scales). Items
  3, 5, 6 and 7 express distrust or a verification habit and are reverse-coded so that higher values mean
  more trust in online information. The registration says "(dis)trust"; the direction is an interpretation.

Estimation, as registered: for each outcome, one linear regression on the eleven treatment indicators
with the Lin (2013) estimator (covariates centred and interacted with the arm indicators). Covariates:
media trust (`media_trust`), political knowledge (`pk_score`), AI usage (`ai_scale`, the share of seven AI
tools used: `chatgpt`, `bing`, `claude`, `character`, `dalle`, `midjourney`, `stable_diff`) and political
interest (`political_interest`), all entered linearly. Observations are weighted by the inverse of the
assignment probability, `ipw = 1 / pr`. Heteroskedasticity-robust (HC2) standard errors; the registration
does not mention clustering and the data have one row per respondent. Two-sided tests, alpha = 0.05. The
registration specifies no multiple-testing correction and none is applied. A random-effects pooled summary
across the eleven arm effects is reported for each outcome as a descriptive summary (not registered).

No exclusions, as registered; the analysis sample is every respondent with an assignment and a non-missing
outcome. Registered target N = 2,000; 2,030 respondents have an assignment.

Not registered, reported as exploratory: effects on the two accuracy components, `fake_score` (share of
the 12 AI-generated posts identified) and `real_score` (share of the 12 authentic posts identified),
which the authors' analysis script also reports.
