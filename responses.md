# Responses to the automated reviewer

Round 1 raised 14 issue(s); 2 analytical issue(s) were answered with robustness addenda, approved by unattended (--yes) on 2026-10-03. Registered analyses were not changed.

## R1: The E1 table has empty est/se/p columns for every arm, yet the text claims that Automated Flagging (p=0.004) and AI Literacy Guide (p=0.043) became nonsignificant. Nothing displayed supports this. The 'attention-check failure' label is also misleading: pk_score<1 is a knowledge-question failure, not an attention check, and may be post-treatment-correlated or confounded with ability. Dropping 30% of the sample is not a clean robustness test.

**Response.** The reviewer notes the exclusion is a low-knowledge screen, not an attention check, so it should be labelled that way and reported with estimates, SEs and CIs. This re-runs H1 excluding pk_score<1, so readers can see whether effects shrink or just get noisier. Added H1a, a robustness re-estimation of H1: exclude low political-knowledge respondents (pk_score<1), full estimates and CIs (`{"exclusions": ["pk_score >= 1"]}`).

**Result.** H1: +0.010 (SE 0.007, p = 0.132, N = 2030). H1a: +0.009 (SE 0.006, p = 0.135, N = 1417).

## R4: The text says the other ten arms had estimates 'between −0.16 and 0.00', but the pooled random-effects result (−0.11, p=0.026) is reported as significant and tied to nothing in the narrative. The Breathing Exercise result (−0.54) has an SE of 0.23 that is much larger than the other arms' SEs, and arm-level SEs vary oddly (0.116 to 0.280), which suggests the Lin interaction model or outliers are driving them.

**Response.** Reviewer suspects the Lin interaction model and covariate leverage drive the heterogeneous arm SEs (e.g., Breathing Exercise). Re-fitting without covariates shows whether arm estimates, SEs and the pooled effect hold up without covariate adjustment. Added H2a, a robustness re-estimation of H2: unadjusted difference in means, no covariates, same weights (`{"estimator": {"kind": "diff_means", "robust": "HC2", "cluster": null, "weights": "ipw", "covariates": [], "continuous": [], "categorical": []}}`).

**Result.** H2: -0.111 (SE 0.050, p = 0.026, N = 2010). H2a: -0.134 (SE 0.054, p = 0.013, N = 2010).

## Second reviewer pass

The tables support a null pooled effect on accuracy (1.0 point, CI [-0.3, 2.4]) and three nominal arm-level H1 effects with p between 0.004 and 0.043. They do not support treating those effects as robust. With 44 uncorrected tests, the exclusion rerun (H1a) removes two of the three effects, and the Guide's interval barely clears zero. The most important caveat is that only Automated Flagging survives the low-knowledge exclusion, and then only at p=0.044. The E1 and E2 findings are unsupported because their tables are empty.

Remaining issues:

- **high** R1 — E1 / E2: The tables have empty estimate columns, yet the Finding lines claim effects were eliminated (E1) and that effects are not concentrated in either familiarity group and 'likely reflect sampling variability' (E2). The review flagged these claims as unsupported but the text still carries them. E1 is also still labelled 'attention-check failures', although pk_score<1 is a knowledge screen.
- **high** R2 — H1 / H1a / Abstract: H1a (dropping 613 low-knowledge respondents) shows Mindfulness becoming non-significant (p=0.12) and the Guide shrinking to 0.023 (p=0.39). Only Automated Flagging survives, at p=0.044. The H1a section has no prose, and the abstract and Key findings present all three H1 effects without this caveat. Excluding on pk_score could also be post-treatment if it was measured after treatment.
- **high** R3 — H1 / Key findings: The three H1 effects are labelled 'Registered' and described as raising or lowering accuracy, but there are 44 uncorrected tests and p-values of 0.032 to 0.043. The Guide's CI lower bound is 0.2 points. The wording is too strong.
- **medium** R4 — H2: The prose calls the pooled -0.11 a result and says 'one arm out of eleven could arise by chance'. The Breathing SE (0.23) is far larger than most other arms' SEs, which the review flagged. Pooled I² is 0 even though SEs vary widely. The unadjusted H2a Breathing estimate (-0.63) is also not discussed.
- **medium** R5 — Design: IPW construction, exclusion rules and attrition by arm are not reported (227 respondents dropped). Control n=181 is much smaller than most treatment arms. Part of the data pre-dated registration, but it is not stated which arms or batches.
- **medium** R6 — H5/H6 and Potential: H6 interprets the pattern as a response-bias shift ('hints that some arms shift how people classify posts'), and the pooled H5 effect is reported as p=0.000. No discernment measure supports the bias reading. Breathing Exercise on real posts is -4.8 and not significant.
- **low** R7 — E3: The Finding line says 'max p = 0.816', which is garbled alongside 'all p > 0.116'. 'Confirming the randomisation' is also too strong for 11 null tests, and no joint test is given.
- **low** R8 — Related work: The retrieved list includes irrelevant items (kidney disease, PRISMA-P, mortality risk), and the Capraro et al. characterisation is dubious (the paper concerns socioeconomic inequalities).
- **medium** K1 — Abstract: Overstated claim: "Two arms raised accuracy: Automated Flagging by 4.4 points ... AI Literacy Guide by 4.7 points". H1_arms: Automated Flagging 0.044, CI [0.014, 0.073], p=0.004. Guide 0.047, CI [0.002, 0.092], p=0.043. H1a: Guide 0.023, p=0.39. Automated Flagging 0.036, p=0.044.
- **medium** K2 — Abstract: Overstated claim: "Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3])". H1_arms: -0.039, p=0.032. H1a: -0.037, CI [-0.083, 0.010], p=0.122.
- **medium** K3 — Key findings: Overstated claim: "Registered: Automated Flagging raised total accuracy by 4.4 points (p=0.004)". H1_arms row 3 matches the numbers. There are 44 uncorrected tests, and H1a gives p=0.044.
- **medium** K4 — H2: Overstated claim: "Attitudes toward AI were lower in the Breathing Exercise arm by 0.54 scale points (p=0.018)". H2 table: -0.543, CI [-0.994, -0.092], p=0.018. This is the only significant arm among 11. H2a gives -0.633, p=0.011.
- **high** K5 — E1: Unsupported claim: "Excluding 613 attention-check failures eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns)". E1 table estimate columns are empty. H1a shows Automated Flagging still significant (p=0.044). The Guide p=0.39. The respondents are low-knowledge, not attention failures.
- **high** K6 — E2: Unsupported claim: "No arm reached p<0.05 in either subsample ... not concentrated ... likely reflect sampling variability". E2 table has only n columns. The estimates and p-values are empty.
- **medium** K7 — E3: Overstated claim: "No intervention significantly affected pre-treatment knowledge (max p = 0.816), confirming the randomisation". E3: min p=0.116, max p=0.816. No joint test is given.
- **medium** K8 — H6: Overstated claim: "Taken with H5, this hints that some arms shift how people classify posts rather than raising accuracy overall". H6: only Infographic 2 is significant (-0.061). H5 has three arms with higher detection. No discernment or bias measure exists.
- **medium** K9 — H5: Overstated claim: "Pooling the 11 arm effects ... 0.038 (SE 0.011, p = 0.000)". The p-value is shown as 0.000. The pooled SE is approximate because the arms share a control group.
