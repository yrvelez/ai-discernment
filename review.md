# Reviewer pass (automated, single pass)

Model: `anthropic/claude-sonnet-5.5`. Mostly consistent reporting of arm estimates, but the report leans on uncorrected borderline findings, contains a pooled-vs-arm inconsistency, hides a large robustness sensitivity, and is truncated.

- **high** R1 (analytical) — H1 / Abstract / Key findings: Headline arm effects (Automated Flagging, Guide, Mindfulness) are presented as findings across 11 arms x 4 outcomes with no multiplicity correction; the Guide (p=0.043) and Mindfulness (p=0.032) would not survive any correction. The abstract states them without hedging in the sentence itself.
  - Suggested fix: Report adjusted p-values (Holm/BH) per outcome family and temper language for borderline arms.
- **high** R2 (presentational) — H1a robustness: The unweighted refit (H1a) shows different estimates (e.g. Flagging +0.008 vs -0.010, Guide +0.004 vs +0.047), implying results are sensitive to IPW, yet the report never discusses it.
  - Suggested fix: Present H1a beside H1, explain the weights, and state that the Guide effect depends on weighting.
- **high** R3 (analytical) — Design and data: Registration came after some data were collected, which is a deviation. It is mentioned only in passing and the tags list no differences. How many responses preceded registration, and whether arms/outcomes were chosen after seeing the data, is not stated.
  - Suggested fix: Flag the timing as a deviation and report the pre-registration batch size and a sensitivity check excluding early data.
- **medium** R4 (presentational) — H1 / Key findings: The Mindfulness arm's mean_arm (0.696) equals its control-adjacent value, yet the estimate is -0.039 with control mean 0.693; the arm means in the summary table don't match the estimates (e.g. Guide mean 0.699 vs +0.047). Adjusted and raw quantities are mixed and unexplained.
  - Suggested fix: Explain that the estimates are covariate-adjusted and weighted while the means are raw, or correct the table.
- **medium** R5 (analytical) — H5: The exploratory H5 prose reports pooled p<0.001 and gains in specific arms, but H1 total accuracy is flat. The AI-detection gain is likely offset by a drop in authentic-content accuracy, suggesting a response bias (more 'AI' answers) rather than better discernment. The report does not say so.
  - Suggested fix: Add a discernment measure (d' or the difference of H5 and H6) and interpret H5 and H6 together.
- **medium** R6 (analytical) — Abstract / H2: The pooled attitude effect (-0.11, p=0.026) is described as a finding while the arm effects are inconsistent and the only significant arm is Breathing Exercise. SEs vary oddly across arms (0.116 to 0.280), and Nudge with n=331 has SE 0.276.
  - Suggested fix: Check for outliers or leverage in the Lin-interacted model, and report the distribution of the outcome.
- **low** R7 (presentational) — H1 text: The claim 'other eight arms within about ±2 points' is false: Nudge is +2.0 and Flagging -1.0, which is fine, but Infographic 2 and others are within range; Provenance/Breathing at 1.5 OK. Pooled CI also uses an approximate SE with a shared control.
  - Suggested fix: Verify the range claim and use a pooled treated-vs-control model for the pooled estimate.
- **low** R8 (presentational) — H6: The H6 section is truncated, with an empty 'Details' block and no table.
  - Suggested fix: Include the H6 model and arm table.

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
