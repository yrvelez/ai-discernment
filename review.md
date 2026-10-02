# Automated review: light pass

Models: orchestrator `anthropic/claude-sonnet-5.5`. The evidence supports a flat pooled effect on total accuracy (+1.0 point, CI spanning zero) and one fairly robust arm result: Automated Flagging, +4.4 weighted and +3.7 unweighted. The Guide and Mindfulness accuracy effects disappear without weights (+0.4 and +0.2), and several other claims are stated more strongly than the tables allow. The registered plan has no multiplicity correction, so about 11 arms across 4 outcomes yield isolated p-values near 0.02-0.04 that are probably chance. The most important caveat is that only Automated Flagging is stable across specifications; the Guide, Mindfulness, Breathing Exercise (H2) and Infographic findings are fragile.

- **high** R1 (analytical) [declined] — H1 / Abstract / Key findings: Headline arm effects (Automated Flagging, Guide, Mindfulness) are presented as findings across 11 arms x 4 outcomes with no multiplicity correction; the Guide (p=0.043) and Mindfulness (p=0.032) would not survive any correction. The abstract states them without hedging in the sentence itself.
  - Suggested fix: Report adjusted p-values (Holm/BH) per outcome family and temper language for borderline arms.
  - Disposition: The plan specifies no multiplicity correction, so adding Holm/BH would change the registered analysis; only tone can be tempered.
- **high** R2 (presentational) [editorial] — H1a robustness: The unweighted refit (H1a) shows different estimates (e.g. Flagging +0.008 vs -0.010, Guide +0.004 vs +0.047), implying results are sensitive to IPW, yet the report never discusses it.
  - Suggested fix: Present H1a beside H1, explain the weights, and state that the Guide effect depends on weighting.
  - Disposition: H1a already exists; the report must discuss the weight dependence in the abstract and key findings.
- **high** R3 (analytical) [address] — Design and data: Registration came after some data were collected, which is a deviation. It is mentioned only in passing and the tags list no differences. How many responses preceded registration, and whether arms/outcomes were chosen after seeing the data, is not stated.
  - Suggested fix: Flag the timing as a deviation and report the pre-registration batch size and a sensitivity check excluding early data.
  - Disposition: A sensitivity re-fit restricted to post-registration batches 3-4 is possible, and the early-batch count should be reported.
- **medium** R4 (presentational) [editorial] — H1 / Key findings: The Mindfulness arm's mean_arm (0.696) equals its control-adjacent value, yet the estimate is -0.039 with control mean 0.693; the arm means in the summary table don't match the estimates (e.g. Guide mean 0.699 vs +0.047). Adjusted and raw quantities are mixed and unexplained.
  - Suggested fix: Explain that the estimates are covariate-adjusted and weighted while the means are raw, or correct the table.
  - Disposition: Estimates are covariate-adjusted and weighted while the arm means are raw; the tables need a note.
- **medium** R5 (analytical) [address] — H5: The exploratory H5 prose reports pooled p<0.001 and gains in specific arms, but H1 total accuracy is flat. The AI-detection gain is likely offset by a drop in authentic-content accuracy, suggesting a response bias (more 'AI' answers) rather than better discernment. The report does not say so.
  - Suggested fix: Add a discernment measure (d' or the difference of H5 and H6) and interpret H5 and H6 together.
  - Disposition: H5 and H6 are already estimated, so a discernment difference or d' can be computed from the same data as an exploratory addition.
- **medium** R6 (analytical) [address] — Abstract / H2: The pooled attitude effect (-0.11, p=0.026) is described as a finding while the arm effects are inconsistent and the only significant arm is Breathing Exercise. SEs vary oddly across arms (0.116 to 0.280), and Nudge with n=331 has SE 0.276.
  - Suggested fix: Check for outliers or leverage in the Lin-interacted model, and report the distribution of the outcome.
  - Disposition: Leverage/outlier checks and the outcome distribution can be reported from existing data; H2a already shows the pooled effect is null.
- **low** R7 (presentational) [editorial] — H1 text: The claim 'other eight arms within about ±2 points' is false: Nudge is +2.0 and Flagging -1.0, which is fine, but Infographic 2 and others are within range; Provenance/Breathing at 1.5 OK. Pooled CI also uses an approximate SE with a shared control.
  - Suggested fix: Verify the range claim and use a pooled treated-vs-control model for the pooled estimate.
  - Disposition: The range claim holds; the clumsy wording should be cleaned up, and H2a already supplies a treated-vs-control pooled model.
- **low** R8 (presentational) [editorial] — H6: The H6 section is truncated, with an empty 'Details' block and no table.
  - Suggested fix: Include the H6 model and arm table.
  - Disposition: The H6 table is present in the report text, so the truncation appears to be a rendering problem to fix.
- **medium** K1 (presentational, claims) [editorial] — Abstract: Overstated claim: "AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2])". H1 row 10: 0.047, p=0.043. In H1a unweighted it is 0.004, CI [-0.023, 0.031]. The abstract does not mention this weight dependence.
  - Suggested fix: State that the effect appears only in the weighted model and is borderline.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K2 (presentational, claims) [editorial] — Abstract: Overstated claim: "Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3])". H1 row 6: -0.039, p=0.032; H1a unweighted +0.002, CI [-0.024, 0.028]. The sign reverses to about zero.
  - Suggested fix: Report as weighting-dependent and not robust.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K3 (presentational, claims) [editorial] — Key findings: Overstated claim: "Pooled attitudes toward AI were slightly lower (-0.11, CI [-0.21, -0.01])". Random-effects pooled -0.111, p=0.026, but the direct treated-vs-control model H2a gives -0.118, SE 0.107, p=0.269, CI [-0.328, 0.091].
  - Suggested fix: Say the pooled effect is not distinguishable from zero in the single treated-vs-control model; the report's claim that H2a matches the pooled row is wrong.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K4 (presentational, claims) [editorial] — Key findings: Overstated claim: "Registered: Mindfulness lowered total accuracy". The effect is significant only in the IPW model (p=0.032) and is null unweighted (H1a).
  - Suggested fix: Add the weighting dependence.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K5 (presentational, claims) [editorial] — Key findings: Overstated claim: "Trust in online information was not distinguishable from unchanged". H4: pooled -0.038, p=0.060; Infographic -0.146, p=0.023. This is inconclusive rather than evidence of no change.
  - Suggested fix: Say the data are inconclusive; effects are small, up to about 0.1 points lower.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K6 (presentational, claims) [editorial] — H2: Overstated claim: "Breathing Exercise lowered attitudes by 0.54 points". H2 row 5: -0.543, p=0.018, with SE 0.230 relative to other arms' 0.12-0.17. Uncorrected, and the other arms are null.
  - Suggested fix: Flag it as a single uncorrected result with an unusually large SE.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K7 (presentational, claims) [editorial] — H5: Overstated claim: "Detection of AI-generated posts was higher in several arms; pooled gain 3.8 points". H5 pooled 0.038, p<0.001, but H1 total accuracy is flat and H6 pooled is -0.7 points. This is consistent with a shift toward answering 'AI' rather than better discernment.
  - Suggested fix: Interpret H5 with H6 and caveat as a possible response bias.
  - Disposition: claim checked against the tables by the orchestrator

## Claim checks (review orchestrator)

- **supported** (Abstract): "Automated Flagging raised total accuracy by 4.4 percentage points (95% CI [1.4, 7.3])" — H1_arms row 3: 0.044, CI [0.014, 0.073], p=0.004; unweighted H1a 0.037, p=0.011.
- **overstated** (Abstract): "AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2])" — H1 row 10: 0.047, p=0.043. In H1a unweighted it is 0.004, CI [-0.023, 0.031]. The abstract does not mention this weight dependence.
- **overstated** (Abstract): "Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3])" — H1 row 6: -0.039, p=0.032; H1a unweighted +0.002, CI [-0.024, 0.028]. The sign reverses to about zero.
- **supported** (Abstract): "The pooled accuracy effect was small and inconclusive (+1.0 point, 95% CI [−0.3, +2.4])" — H1 pooled 0.010, SE 0.007, p=0.132; the CI is consistent with this. The unweighted pooled estimate is 0.012, p=0.004.
- **overstated** (Key findings): "Pooled attitudes toward AI were slightly lower (-0.11, CI [-0.21, -0.01])" — Random-effects pooled -0.111, p=0.026, but the direct treated-vs-control model H2a gives -0.118, SE 0.107, p=0.269, CI [-0.328, 0.091].
- **supported** (Key findings): "Flagging and AI Literacy Infographic 2 lowered confidence in AI detection" — H3: Flagging -0.525, p=0.012; Infographic 2 -0.686, p=0.010. The pooled estimate is inconclusive and the tests are uncorrected.
- **overstated** (Key findings): "Registered: Mindfulness lowered total accuracy" — The effect is significant only in the IPW model (p=0.032) and is null unweighted (H1a).
- **overstated** (Key findings): "Trust in online information was not distinguishable from unchanged" — H4: pooled -0.038, p=0.060; Infographic -0.146, p=0.023. This is inconclusive rather than evidence of no change.
- **supported** (H1): "The other eight arms were within about ±2 points of control" — H1 estimates range from -0.010 to +0.020 for the other eight arms.
- **overstated** (H2): "Breathing Exercise lowered attitudes by 0.54 points" — H2 row 5: -0.543, p=0.018, with SE 0.230 relative to other arms' 0.12-0.17. Uncorrected, and the other arms are null.
- **overstated** (H5): "Detection of AI-generated posts was higher in several arms; pooled gain 3.8 points" — H5 pooled 0.038, p<0.001, but H1 total accuracy is flat and H6 pooled is -0.7 points. This is consistent with a shift toward answering 'AI' rather than better discernment.

## Editorial guidance

- Put the weight dependence of the Guide and Mindfulness accuracy effects in the abstract and key findings.
- Correct the claim that H2a matches the pooled attitude result: the direct model gives p=0.269.
- Report how many responses preceded registration and flag the timing as a deviation.
- Interpret H5 and H6 together; do not present the AI-detection gain as improved discernment.
- Say trust effects are inconclusive, not unchanged.
- Explain that estimates are adjusted and weighted while arm means are raw, and describe the IPW weights.

## Unresolved questions (candidates for extensions)

- U1: Do Automated Flagging labels improve discernment (sensitivity and specificity) rather than shifting response bias, in a pre-registered replication with adequate arm sizes? (Arms are small, the tests uncorrected, and only total accuracy was registered; the H1 and H5/H6 patterns cannot separate discernment from bias.)
- U2: Would the Guide and Mindfulness effects replicate, and which weighting model reflects the target population? (The effects depend on IPW and no single dataset can show which weighting specification is correct.)

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
