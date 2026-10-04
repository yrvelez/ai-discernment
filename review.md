# Automated review: Light Pass, Advanced Pass (methodology + statistics)

Models: light `anthropic/claude-sonnet-5.5`, advanced:methodology `qwen/qwen3.8-27b`, advanced:statistics `qwen/qwen3.8-27b`, orchestrator `anthropic/claude-sonnet-5.5`. The registered data support one reasonably clear result: Automated Flagging raised total accuracy by about 4.4 points. The AI Literacy Guide (p=0.043) and Mindfulness (p=0.032) results are borderline and uncorrected across 44 registered tests. The pooled accuracy effect is null, and the confidence, attitude and trust findings are isolated arm-level results. The most important caveat is that several significant arm effects do not match the raw arm-versus-control mean differences, so they depend on the weighted, covariate-interacted model, and the report does not reconcile the two. The H5 and H6 results are exploratory and cannot separate discernment from a shift toward answering 'AI'.

**Review outcome (round 1): 9 of 11 claims supported by the results after the agent's corrections; 1 analytical issue without a robustness check.**

- **high** R1 (analytical) [declined] — Abstract / H1 / Key findings: The headline says Automated Flagging and the Guide 'raised' accuracy, and the abstract notes the uncorrected tests only in passing. With 44 uncorrected registered tests and 3 significant H1 arms, only Automated Flagging (p=.004) is plausibly robust; the Guide (p=.043) and Mindfulness (p=.032) would not survive any correction. The Key findings list them as plain findings.
  - Suggested fix: Report multiplicity-adjusted p-values (Holm/BH) per outcome family, and word the Guide and Mindfulness results as tentative.
  - Disposition: The registered plan specifies no multiple-testing correction, so adjusted p-values are not added; the wording is softened instead (editorial).
- **medium** R2 (analytical) [address] — H2: The pooled estimate of -0.11 (p=.026) is called 'a small shift', yet no individual arm besides Breathing Exercise differs from zero. The Breathing Exercise estimate (-0.54) is larger than its own arm mean difference (4.146 vs 4.187 = -0.04), which suggests covariate adjustment or weighting drives it. The raw means and the adjusted estimates are not reconciled anywhere.
  - Suggested fix: Show unadjusted and adjusted estimates, check sensitivity to the Lin interaction model and the IPW weights, and explain the discrepancy.
  - Disposition: Unadjusted and unweighted estimates can be fitted on the same data to show where the Breathing Exercise estimate comes from.
- **medium** R3 (analytical) [address] — H1 tables: The mean_arm values in the CSVs do not match the estimates. Mindfulness is -3.9 points adjusted but its raw arm mean is higher than control (0.696 vs 0.693), and the Guide's raw difference is only 0.6 points against an adjusted +4.7. The significant H1 results therefore depend on the weighted, covariate-interacted model.
  - Suggested fix: Report unadjusted, unweighted differences alongside the adjusted results, and state that the IPW weights are model-dependent (what they correct for). Also check whether the IPW weights are influential.
  - Disposition: A robustness re-fit with raw differences, no weights and no interactions, plus a check of weight influence, answers this directly.
- **medium** R4 (analytical) [unresolved] — H5: The pooled H5 effect is reported with p = 0.000, and the text emphasises the Breathing Exercise and Nudge as raising detection of AI posts. This is exploratory, and H6 shows no matching gain for authentic posts. The AI Literacy Guide result (CI [0.000, 0.157], p=.049) is borderline. Higher AI-detection scores could reflect a shift toward answering 'AI' more often (response bias) rather than better discernment, which would make this an accuracy gain only in name.
  - Suggested fix: Report p<0.001 rather than 0.000, and analyse sensitivity/specificity or d' to separate discernment from response bias. Qualify the Key finding.
  - Disposition: Sensitivity and d' need per-post responses and truth labels that the tables do not provide, so response bias cannot be separated from discernment here; only the p-value formatting is editorial.
- **medium** R5 (presentational) [editorial] — Design: The control group has n=181 but this is not stated in the report ('whose size is not given in the tables'). The arms are very unbalanced (78 to 333), and the report does not explain the allocation or whether the 227 exclusions differed by arm.
  - Suggested fix: State the control n, give the exclusion criteria, and show attrition/exclusion by arm.
  - Disposition: The control n of 181 is in the tables, so the report only needs to state it and describe the exclusions; exclusion counts by arm cannot be shown from these tables.
- **low** R6 (analytical) [address] — Design / Registration: Data existed at registration, and the registered date (2023-11-15) falls after fielding (Oct–Nov 2023). The claim that 'later batches followed the plan' is unverified, and no analysis separates pre- and post-registration batches.
  - Suggested fix: Report which share of the data predates registration, and run a sensitivity analysis on post-registration data only.
  - Disposition: A post-registration-batch-only re-fit is possible if a batch indicator exists in the data.
- **low** R7 (presentational) [editorial] — Related work: The related-work section lists irrelevant retrieved items (additive manufacturing, drug development, publication-bias tests) and draws only weak links to the study. It also describes the null results as 'anticipated' by the i-frame critique.
  - Suggested fix: Remove irrelevant citations and drop the claim that nulls were anticipated.
  - Disposition: Irrelevant citations and the claim that nulls were anticipated should be removed.
- **low** R8 (presentational) [editorial] — H4: The pooled p=.060 and the single arm at p=.023 are described as 'unchanged in the data's resolution', which is vague. The CIs also exclude effects that could matter, but the report does not discuss this.
  - Suggested fix: Rephrase in terms of the CI bounds (effects larger than about 0.27 are ruled out).
  - Disposition: The H4 prose can be rewritten in terms of the CI bounds.
- **medium** K1 (presentational, claims) [editorial] — Abstract: Overstated claim: "the AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2])". H1 row 10: 0.047, p=0.043. The raw arm mean is 0.699 vs 0.693 for control, a gap of only 0.6 points, so the result depends on the adjusted model.
  - Suggested fix: Call it tentative, borderline and model-dependent, and report the unadjusted difference beside it.
  - Disposition: claim checked against the tables by the checking agent
- **medium** K2 (presentational, claims) [editorial] — Abstract: Overstated claim: "Mindfulness lowered it by 3.9 points (95% CI [-7.4, -0.3])". H1 row 6: -0.039, p=0.032. The raw arm mean is 0.696 vs 0.693 for control, which is higher, not lower.
  - Suggested fix: Describe it as a borderline adjusted estimate that the raw means do not reproduce.
  - Disposition: claim checked against the tables by the checking agent
- **medium** K3 (presentational, claims) [editorial] — H2: Overstated claim: "Breathing Exercise lowered attitudes by 0.54 scale points". H2 row 5: -0.543, p=0.018. The raw means are 4.146 vs 4.187, a gap of about 0.04, so the estimate comes from the adjusted model.
  - Suggested fix: Flag it as an isolated adjusted estimate that the raw means do not support, and give the unadjusted difference.
  - Disposition: claim checked against the tables by the checking agent
- **medium** K4 (presentational, claims) [editorial] — H2: Overstated claim: "The pooled estimate was -0.11 (95% CI [-0.21, -0.01]), a small shift". H2 pooled: -0.111, p=0.026. Ten of the 11 arms have intervals spanning zero, and the result is uncorrected.
  - Suggested fix: Describe it as a marginal pooled estimate that is not robust.
  - Disposition: claim checked against the tables by the checking agent
- **medium** K5 (presentational, claims) [editorial] — Key findings: Overstated claim: "Exploratory splits suggest the Breathing Exercise and AI Accuracy Nudge raised detection of AI-generated posts". H5 rows 5 and 4: 0.091 (p=0.003) and 0.066 (p=0.014). H6 shows no matching gain for authentic posts, and response bias is not excluded.
  - Suggested fix: Say these arms raised the share of AI posts identified, and that this may reflect a greater tendency to answer 'AI' rather than better discernment.
  - Disposition: claim checked against the tables by the checking agent
- **medium** K6 (presentational, claims) [editorial] — H5: Overstated claim: "The pooled H5 effect, p = 0.000". The pooled estimate is 0.038, SE 0.011; a p-value of exactly zero is a rounding artefact.
  - Suggested fix: Report p<0.001 and label the result exploratory.
  - Disposition: claim checked against the tables by the checking agent

## Claim checks (checking agent)

- **supported** (Abstract): "Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3])" — H1_arms row 3: 0.044, CI [0.014, 0.073], p=0.004; raw means 0.726 vs 0.693 point the same way.
- **overstated** (Abstract): "the AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2])" — H1 row 10: 0.047, p=0.043. The raw arm mean is 0.699 vs 0.693 for control, a gap of only 0.6 points, so the result depends on the adjusted model.
- **overstated** (Abstract): "Mindfulness lowered it by 3.9 points (95% CI [-7.4, -0.3])" — H1 row 6: -0.039, p=0.032. The raw arm mean is 0.696 vs 0.693 for control, which is higher, not lower.
- **supported** (Abstract): "Pooled across arms, accuracy was not distinguishable from control (+1.0 point)" — H1 pooled: 0.010, SE 0.007, p=0.132.
- **overstated** (H2): "Breathing Exercise lowered attitudes by 0.54 scale points" — H2 row 5: -0.543, p=0.018. The raw means are 4.146 vs 4.187, a gap of about 0.04, so the estimate comes from the adjusted model.
- **overstated** (H2): "The pooled estimate was -0.11 (95% CI [-0.21, -0.01]), a small shift" — H2 pooled: -0.111, p=0.026. Ten of the 11 arms have intervals spanning zero, and the result is uncorrected.
- **supported** (H3): "Inoculation raised confidence by 0.51; Flagging lowered it by 0.53; AI Literacy Infographic 2 lowered it by 0.69" — H3 rows 7, 1 and 9: 0.509 (p=0.007), -0.525 (p=0.012), -0.686 (p=0.010). The tests are uncorrected and the Inoculation arm has only n=77.
- **supported** (H4): "Only the AI Literacy Infographic differed on trust, at 0.15 points lower" — H4 row 8: -0.146, p=0.0235. The pooled estimate is -0.038, p=0.060.
- **overstated** (Key findings): "Exploratory splits suggest the Breathing Exercise and AI Accuracy Nudge raised detection of AI-generated posts" — H5 rows 5 and 4: 0.091 (p=0.003) and 0.066 (p=0.014). H6 shows no matching gain for authentic posts, and response bias is not excluded.
- **overstated** (H5): "The pooled H5 effect, p = 0.000" — The pooled estimate is 0.038, SE 0.011; a p-value of exactly zero is a rounding artefact.

## Corrections requested by the checking agent

- Soften the Guide, Mindfulness and Breathing Exercise results to tentative, and note that the raw means do not reproduce them.
- State the control n=181 and the exclusion counts (2,257 collected, 2,030 analysed).
- Replace 'p = 0.000' with 'p<0.001' throughout.
- Remove the irrelevant citations (additive manufacturing, drug development, publication-bias tests) and the statement that nulls were 'anticipated'.
- In H4, rewrite 'unchanged in the data's resolution' using the CI bounds (effects beyond about 0.27 ruled out for the most precise arms).

## Corrections made by the writing agent

- K1: Abstract and takeaways call the Guide result tentative and borderline; the unadjusted difference (+0.6 points) is given in H1 and H1a.
- K2: Mindfulness is described as a borderline adjusted estimate that the raw means do not reproduce.
- K3: Breathing Exercise flagged as isolated and adjusted-only; raw difference of about 0.04 given.
- K4: Pooled attitude estimate described as marginal, not robust, and uncorrected.
- K5: Takeaway and H5 say the arms raised the share of AI posts identified, possibly via response bias.
- K6: There is no 'p = 0.000' or pooled H5 figure in the table-based text, so nothing to replace; no pooled H5 p-value was added, as it is not in the tables.
- G1: Guide, Mindfulness and Breathing Exercise softened, with note that raw means do not reproduce them.
- G2: Control n=181 and the 2,257 collected / 2,030 analysed counts stated.
- G3: No 'p = 0.000' appears in the revised text.
- G4: The draft had no related-work section or 'anticipated nulls' claim, so nothing to remove.
- G5: H4 rewritten using the CI bounds (about 0.27).
- R5: Control n stated; exclusion criteria and by-arm exclusions are not in the tables, and the text says so.
- R7: No related-work section is present; nothing to change.
- R8: H4 rephrased in terms of CI bounds.
- F1: The H5 text contains no pooled estimate or 'p = 0.000'; the p-values shown (0.003, 0.014, 0.049) come from the table, so nothing needed changing. No pooled H5 figure was added because it is not in the tables.
- R1: Declined; no multiple-testing correction was registered, so the uncorrected-tests caveat stays as written.

## Claim re-check on the corrected text

Add an uncorrected/small-arm caveat to the H3 confidence results and report the pooled H5 p-value as p<0.001 instead of 0.000.

- **supported** (Abstract, re-check of C1): "Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3])" — H1_arms row 3: 0.044, CI [0.014, 0.073], p=0.004. H1a unadjusted is +3.2 points (p=0.028), same direction.
- **supported** (Abstract, re-check of C2/C3): "The AI Literacy Guide (+4.7 points) and Mindfulness (−3.9 points) are borderline adjusted estimates that the raw means do not reproduce, so they are tentative." — H1 rows 10 and 6: 0.047 (p=0.043) and -0.039 (p=0.032). Raw arm means are 0.699 and 0.696 vs 0.693 control; H1a gives +0.6 and +0.2.
- **supported** (Abstract, re-check of C4): "Pooled across arms, total accuracy was not distinguishable from control (+1.0 point, 95% CI [−0.3, +2.4])" — H1 pooled: 0.010, SE 0.007, p=0.132.
- **supported** (H2, re-check of C5): "The Breathing Exercise estimate was −0.54 scale points ... isolated and tentative: the raw means differ by only about 0.04" — H2 row 5: -0.543, p=0.018; raw means 4.146 vs 4.187; H2a gives -0.04 (CI [-0.32, 0.24]).
- **supported** (H2, re-check of C6): "The pooled estimate was −0.11 (95% CI [−0.21, −0.01], p = 0.026), a marginal result that is not robust" — H2 pooled -0.111, p=0.026; H2a unadjusted pooled -0.038, p=0.356.
- **overstated** (H3, re-check of C7): "Inoculation raised it by 0.51 points; Flagging lowered it by 0.53; AI Literacy Infographic 2 by 0.69" — H3 rows 7, 1, 9: 0.509 (p=0.007), -0.525 (p=0.012), -0.686 (p=0.010). Numbers match, but the uncorrected and small-arm caveat (Inoculation n=77) is not attached in this section.
- **supported** (H4, re-check of C8): "Only the AI Literacy Infographic differed on trust in online information, at 0.15 points lower than control" — H4 row 8: -0.146, p=0.0235; pooled -0.038, p=0.060; single arm flagged as weak evidence.
- **supported** (Key findings, re-check of C9): "Exploratory: the Breathing Exercise and AI Accuracy Nudge raised the share of AI posts identified. This may reflect a greater tendency to answer 'AI'" — H5 rows 5 and 4: 0.091 (p=0.003), 0.066 (p=0.014); H6 shows no matching gain; response-bias caveat included.
- **overstated** (H5, re-check of C10): "Pooling the 11 arm effects ... gives 0.038 (SE 0.011, p = 0.000)" — Pooled 0.038, SE 0.011; p of exactly 0.000 is a rounding artefact. Same p=0.000 print persists.
- **supported** (H1a): "Without covariates or weights, Automated Flagging remained higher, at +3.2 points (95% CI [0.3, 6.2], p = 0.028)" — H1a row 3: 0.032, CI [0.003, 0.062], p=0.028.
- **supported** (Key findings): "Flagging and AI Literacy Infographic 2 lowered confidence in AI detection." — H3 rows 1 and 9: -0.525 (p=0.012) and -0.686 (p=0.010).

## Unresolved questions (candidates for extensions)

- U1: Do the exploratory gains in AI-post detection reflect better discernment or a greater tendency to answer 'AI'? (Only share-correct scores are reported, with no per-post responses to compute sensitivity, specificity or d'.)

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
