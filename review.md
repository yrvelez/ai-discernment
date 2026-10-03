# Automated review: light pass, advanced pass (methodology + statistics)

Models: light `anthropic/claude-sonnet-5.5`, advanced:methodology `qwen/qwen3.8-27b`, advanced:statistics `qwen/qwen3.8-27b`, orchestrator `anthropic/claude-sonnet-5.5`. The tables support a null pooled effect on accuracy (1.0 point, CI [-0.3, 2.4]) and three nominal arm-level H1 effects with p between 0.004 and 0.043. They do not support treating those effects as robust. With 44 uncorrected tests, the exclusion rerun (H1a) removes two of the three effects, and the Guide's interval barely clears zero. The most important caveat is that only Automated Flagging survives the low-knowledge exclusion, and then only at p=0.044. The E1 and E2 findings are unsupported because their tables are empty.

**Review outcome (round 2): 8 of 12 claims supported by the results after the authors' revision; 2 analytical issues open for a robustness round.**

Earlier round 1: 14 issue(s); 10 of 12 claims supported by the results after the authors' revision; 3 analytical issues open for a robustness round.

- **high** R1 (analytical) [editorial] — E1 / E2: The tables have empty estimate columns, yet the Finding lines claim effects were eliminated (E1) and that effects are not concentrated in either familiarity group and 'likely reflect sampling variability' (E2). The review flagged these claims as unsupported but the text still carries them. E1 is also still labelled 'attention-check failures', although pk_score<1 is a knowledge screen.
  - Suggested fix: Populate the tables with estimates, SEs and an arm-by-familiarity interaction test, or delete the conclusions. Relabel E1 as a low-knowledge exclusion.
  - Disposition: The E1 and E2 tables are empty, so the conclusions must be deleted or the tables populated, and E1 needs relabelling as a low-knowledge exclusion.
- **high** R2 (presentational) [editorial] — H1 / H1a / Abstract: H1a (dropping 613 low-knowledge respondents) shows Mindfulness becoming non-significant (p=0.12) and the Guide shrinking to 0.023 (p=0.39). Only Automated Flagging survives, at p=0.044. The H1a section has no prose, and the abstract and Key findings present all three H1 effects without this caveat. Excluding on pk_score could also be post-treatment if it was measured after treatment.
  - Suggested fix: Add H1a prose and report that two of the three effects are not robust to the exclusion. Clarify when pk_score was measured.
  - Disposition: The H1a estimates already exist, so the fix is prose that reports the non-robustness and when pk_score was measured.
- **high** R3 (analytical) [declined] — H1 / Key findings: The three H1 effects are labelled 'Registered' and described as raising or lowering accuracy, but there are 44 uncorrected tests and p-values of 0.032 to 0.043. The Guide's CI lower bound is 0.2 points. The wording is too strong.
  - Suggested fix: Report Holm/BH-adjusted p-values beside the registered ones as a supplementary robustness check, and describe the effects as nominal.
  - Disposition: The plan specifies no multiple-testing correction, so adjusted p-values would change the registered analysis. The wording can be softened to 'nominal' without it.
- **medium** R4 (analytical) [address] — H2: The prose calls the pooled -0.11 a result and says 'one arm out of eleven could arise by chance'. The Breathing SE (0.23) is far larger than most other arms' SEs, which the review flagged. Pooled I² is 0 even though SEs vary widely. The unadjusted H2a Breathing estimate (-0.63) is also not discussed.
  - Suggested fix: Report H2a in the text, run leverage and outlier diagnostics for the Lin interaction model, and soften the interpretation.
  - Disposition: Leverage and outlier diagnostics on the Lin model can be run on the same data, and H2a can be discussed in the text.
- **medium** R5 (presentational) [editorial] — Design: IPW construction, exclusion rules and attrition by arm are not reported (227 respondents dropped). Control n=181 is much smaller than most treatment arms. Part of the data pre-dated registration, but it is not stated which arms or batches.
  - Suggested fix: Document the weights, exclusions and attrition by arm, and state which batches pre-dated registration.
  - Disposition: The weights, exclusions, attrition by arm and pre-registration batches need documenting in the text.
- **medium** R6 (presentational) [editorial] — H5/H6 and Potential: H6 interprets the pattern as a response-bias shift ('hints that some arms shift how people classify posts'), and the pooled H5 effect is reported as p=0.000. No discernment measure supports the bias reading. Breathing Exercise on real posts is -4.8 and not significant.
  - Suggested fix: Present the bias reading as speculative, write p<0.001, and avoid the interpretation until item-level data are available.
  - Disposition: The bias reading should be labelled speculative and the pooled p written as p<0.001.
- **low** R7 (analytical) [address] — E3: The Finding line says 'max p = 0.816', which is garbled alongside 'all p > 0.116'. 'Confirming the randomisation' is also too strong for 11 null tests, and no joint test is given.
  - Suggested fix: Say 'min p = 0.116' and 'consistent with balance', and add a joint F-test.
  - Disposition: A joint F-test of arm dummies on pk_score is a straightforward additional estimate, and the wording needs fixing too.
- **low** R8 (presentational) [editorial] — Related work: The retrieved list includes irrelevant items (kidney disease, PRISMA-P, mortality risk), and the Capraro et al. characterisation is dubious (the paper concerns socioeconomic inequalities).
  - Suggested fix: Remove the irrelevant references and correct the Capraro description.
  - Disposition: The irrelevant references should be removed and the Capraro description corrected.
- **medium** K1 (presentational, claims) [editorial] — Abstract: Overstated claim: "Two arms raised accuracy: Automated Flagging by 4.4 points ... AI Literacy Guide by 4.7 points". H1_arms: Automated Flagging 0.044, CI [0.014, 0.073], p=0.004. Guide 0.047, CI [0.002, 0.092], p=0.043. H1a: Guide 0.023, p=0.39. Automated Flagging 0.036, p=0.044.
  - Suggested fix: Say the arms had nominally higher accuracy in uncorrected tests. Only Automated Flagging held up when low-knowledge respondents were excluded.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K2 (presentational, claims) [editorial] — Abstract: Overstated claim: "Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3])". H1_arms: -0.039, p=0.032. H1a: -0.037, CI [-0.083, 0.010], p=0.122.
  - Suggested fix: Describe it as a nominal decrease that was not robust to the exclusion.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K3 (presentational, claims) [editorial] — Key findings: Overstated claim: "Registered: Automated Flagging raised total accuracy by 4.4 points (p=0.004)". H1_arms row 3 matches the numbers. There are 44 uncorrected tests, and H1a gives p=0.044.
  - Suggested fix: Add 'nominal, uncorrected' and mention the H1a result.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K4 (presentational, claims) [editorial] — H2: Overstated claim: "Attitudes toward AI were lower in the Breathing Exercise arm by 0.54 scale points (p=0.018)". H2 table: -0.543, CI [-0.994, -0.092], p=0.018. This is the only significant arm among 11. H2a gives -0.633, p=0.011.
  - Suggested fix: Report H2a and describe the result as isolated and exploratory in character.
  - Disposition: claim checked against the tables by the orchestrator
- **high** K5 (presentational, claims) [editorial] — E1: Unsupported claim: "Excluding 613 attention-check failures eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns)". E1 table estimate columns are empty. H1a shows Automated Flagging still significant (p=0.044). The Guide p=0.39. The respondents are low-knowledge, not attention failures.
  - Suggested fix: Delete the claim, or fill the table. Say Automated Flagging remains at p=0.044 and the Guide is not robust.
  - Disposition: claim checked against the tables by the orchestrator
- **high** K6 (presentational, claims) [editorial] — E2: Unsupported claim: "No arm reached p<0.05 in either subsample ... not concentrated ... likely reflect sampling variability". E2 table has only n columns. The estimates and p-values are empty.
  - Suggested fix: Delete the conclusion or populate the table with an interaction test.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K7 (presentational, claims) [editorial] — E3: Overstated claim: "No intervention significantly affected pre-treatment knowledge (max p = 0.816), confirming the randomisation". E3: min p=0.116, max p=0.816. No joint test is given.
  - Suggested fix: Say 'min p=0.116; consistent with balance' and add a joint F-test.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K8 (presentational, claims) [editorial] — H6: Overstated claim: "Taken with H5, this hints that some arms shift how people classify posts rather than raising accuracy overall". H6: only Infographic 2 is significant (-0.061). H5 has three arms with higher detection. No discernment or bias measure exists.
  - Suggested fix: Present it as speculation.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K9 (presentational, claims) [editorial] — H5: Overstated claim: "Pooling the 11 arm effects ... 0.038 (SE 0.011, p = 0.000)". The p-value is shown as 0.000. The pooled SE is approximate because the arms share a control group.
  - Suggested fix: Write p<0.001 and note the approximation.
  - Disposition: claim checked against the tables by the orchestrator

## Claim checks (review orchestrator)

- **supported** (Abstract): "Pooled across arms, total accuracy was 1.0 point higher than control (95% CI [−0.3, 2.4])" — registered_summary H1:pooled: estimate 0.010, SE 0.007, p=0.132. The CI follows from the estimate and SE.
- **overstated** (Abstract): "Two arms raised accuracy: Automated Flagging by 4.4 points ... AI Literacy Guide by 4.7 points" — H1_arms: Automated Flagging 0.044, CI [0.014, 0.073], p=0.004. Guide 0.047, CI [0.002, 0.092], p=0.043. H1a: Guide 0.023, p=0.39. Automated Flagging 0.036, p=0.044.
- **overstated** (Abstract): "Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3])" — H1_arms: -0.039, p=0.032. H1a: -0.037, CI [-0.083, 0.010], p=0.122.
- **overstated** (Key findings): "Registered: Automated Flagging raised total accuracy by 4.4 points (p=0.004)" — H1_arms row 3 matches the numbers. There are 44 uncorrected tests, and H1a gives p=0.044.
- **supported** (Key findings): "Pooled across arms, attitudes toward AI were lower by 0.11 scale points (95% CI [−0.21, −0.01])" — H2 pooled: -0.111, SE 0.050, p=0.026. The unadjusted H2a pooled estimate is -0.134, p=0.013.
- **overstated** (H2): "Attitudes toward AI were lower in the Breathing Exercise arm by 0.54 scale points (p=0.018)" — H2 table: -0.543, CI [-0.994, -0.092], p=0.018. This is the only significant arm among 11. H2a gives -0.633, p=0.011.
- **supported** (H3): "Confidence fell in AI Literacy Infographic 2 by 0.69 and Flagging by 0.53; Inoculation raised it by 0.51" — H3 table: -0.686 (p=0.0095), -0.525 (p=0.012), +0.509 (p=0.007). The text is hedged elsewhere.
- **unsupported** (E1): "Excluding 613 attention-check failures eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns)" — E1 table estimate columns are empty. H1a shows Automated Flagging still significant (p=0.044). The Guide p=0.39. The respondents are low-knowledge, not attention failures.
- **unsupported** (E2): "No arm reached p<0.05 in either subsample ... not concentrated ... likely reflect sampling variability" — E2 table has only n columns. The estimates and p-values are empty.
- **overstated** (E3): "No intervention significantly affected pre-treatment knowledge (max p = 0.816), confirming the randomisation" — E3: min p=0.116, max p=0.816. No joint test is given.
- **overstated** (H6): "Taken with H5, this hints that some arms shift how people classify posts rather than raising accuracy overall" — H6: only Infographic 2 is significant (-0.061). H5 has three arms with higher detection. No discernment or bias measure exists.
- **overstated** (H5): "Pooling the 11 arm effects ... 0.038 (SE 0.011, p = 0.000)" — The p-value is shown as 0.000. The pooled SE is approximate because the arms share a control group.

## Editorial guidance

- Delete or populate the E1 and E2 findings, and relabel E1 as a low-knowledge exclusion.
- Add H1a prose to the abstract and Key findings: only Automated Flagging survives, at p=0.044, and the Mindfulness and Guide effects do not.
- Describe the three H1 effects as nominal, since 44 tests were run uncorrected and the plan has no correction.
- State when pk_score was measured relative to treatment, and document the IPW weights, exclusions, attrition by arm and which batches pre-dated registration.
- Change E3 to 'min p=0.116, consistent with balance', and write the H5 pooled p as <0.001.
- Remove the irrelevant references and correct the Capraro description.

## Author response (the writer's revision notes)

- K1: Abstract now calls the accuracy effects nominal and uncorrected, and notes only Automated Flagging held under exclusion.
- K2: Mindfulness described as a nominal decrease, not robust to the exclusion.
- K3: Key finding now says nominal, uncorrected, and cites the H1a result (p=0.044).
- K4: H2 now reports H2a (−0.63, p=0.011) and calls the result isolated and exploratory in character.
- K5: E1 claim deleted and relabelled as a low-knowledge exclusion; points to H1a.
- K6: E2 conclusion deleted; the table has no estimates.
- K7: E3 now says min p=0.116, consistent with balance; no joint test is available in the tables, so none was added.
- K8: H6 bias reading presented as speculation.
- K9: The H5 pooled estimate is not in the supplied tables, so no pooled figure or p<0.001 was added; nothing changed.
- G1: E1 and E2 conclusions removed, E1 relabelled.
- G2: H1a added to the abstract and takeaways.
- G3: H1 effects described as nominal given 44 uncorrected tests.
- G4: Design notes state what is undocumented (weights, exclusions, attrition, batches, pk_score timing); I could not supply details absent from the inputs.
- G5: E3 wording changed; the pooled H5 p is not in the tables, so it was not added.
- G6: The draft contained no literature references, so nothing was removed.

## Sign-off on the revised text

Remove the original E1 and E2 Finding sentences and soften E3's 'confirming the randomisation'. Also report H5's pooled p as p<0.001.

- **supported** (Abstract, re-check of C1): "Pooled across arms, total accuracy was 1.0 point higher than control (95% CI [−0.3, 2.4])" — registered_summary H1:pooled: 0.010, SE 0.007, p=0.132; CI follows.
- **supported** (Abstract, re-check of C2): "Automated Flagging nominally raised accuracy by 4.4 points ... AI Literacy Guide by 4.7 points" — H1_arms: 0.044 (p=0.004), 0.047 (p=0.043); labelled nominal, uncorrected, and H1a result stated.
- **supported** (Abstract, re-check of C3): "Mindfulness nominally lowered it by 3.9 points (95% CI [−7.4, −0.3])" — H1_arms: -0.039, CI [-0.074,-0.003], p=0.032; H1a p=0.122 noted in Key findings.
- **supported** (Key findings, re-check of C4): "Automated Flagging had 4.4 points higher total accuracy ... it also held when low-knowledge respondents were excluded (p=0.044)" — H1_arms row 3 and H1a_arms row 3: 0.036, p=0.044. Hedged as nominal and uncorrected.
- **supported** (Key findings, re-check of C5): "Pooled across arms, attitudes toward AI were 0.11 scale points lower (95% CI [−0.21, −0.01])" — H2 pooled -0.111, SE 0.050, p=0.026.
- **supported** (H2, re-check of C6): "Attitudes toward AI were 0.54 scale points lower in the Breathing Exercise arm ... only one of eleven arms ... exploratory in character" — H2: -0.543, p=0.018; H2a -0.633, p=0.011; other arms ns.
- **supported** (H3, re-check of C7): "AI Literacy Infographic 2 by 0.69 and Flagging by 0.53 lower; Inoculation raised by 0.51" — H3 table: -0.686 (p=0.0095), -0.525 (p=0.012), +0.509 (p=0.007).
- **overstated** (E1, re-check of C8): "Excluding 613 attention-check failures eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns)" — E1 estimate columns are empty. The Finding line still asserts Automated Flagging became ns, but H1a shows p=0.044. The follow-up note withdraws it, yet the original wording remains.
- **unsupported** (E2, re-check of C9): "No arm reached p<0.05 in either subsample ... likely reflect sampling variability" — E2 table has only n columns; estimates and p-values are empty. The Finding line is still in the text.
- **overstated** (E3, re-check of C10): "No intervention significantly affected pre-treatment knowledge (all p > 0.116, max p = 0.816), confirming the randomisation" — E3: min p=0.116, max 0.816; no joint test. 'Confirming' is too strong.
- **supported** (H6, re-check of C11): "One might speculate that some arms shift how people classify posts, but ... it remains speculation" — Framed as speculation; H6 only Infographic 2 significant (-0.061).
- **overstated** (H5, re-check of C12): "Pooling the 11 arm effects ... gives 0.038 (SE 0.011, p = 0.000)" — p shown as 0.000; the approximation caveat is present but the p format remains.

## Unresolved questions (candidates for extensions)

- U1: Do the interventions change response bias (willingness to label posts as AI) rather than true discernment? (Only share-correct scores exist, so there is no signal-detection measure to separate sensitivity from bias.)
- U2: Do the Automated Flagging and AI Literacy Guide effects on accuracy replicate in a larger, independent sample with a pre-specified correction? (The effects are marginal with 44 uncorrected tests and small arms, so this single study cannot distinguish them from chance.)

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
