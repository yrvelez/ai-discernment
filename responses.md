# Responses to the automated reviewer

Round 1 raised 7 issue(s); 2 analytical issue(s) were answered with robustness addenda, approved by unattended (--yes) on 2026-10-01. Registered analyses were not changed.

## R4: The random-effects pooling treats arms as independent although they share one control group. The report concedes the SE is approximate. H2's pooled effect (p=0.026), which is highlighted as a registered finding, rests on this approximation, and its I² is 0.

**Response.** Random-effects pooling treats arms as independent despite the shared control group. A single two-arm model comparing all treated respondents with control, using robust SEs, accounts for the shared control directly. Added H2a, a robustness re-estimation of H2: collapse all treated arms vs control in one model (`{"collapse_arms": true, "pooled": false}`).

**Result.** H2: -0.111 (SE 0.050, p = 0.026, N = 2010). H2a: -0.118 (SE 0.107, p = 0.269, N = 2010).

## R5: The weights are labelled 'inverse probability' without saying what they correct for, such as assignment or attrition. Unequal arm sizes (78 to 333) and the 227 exclusions are not explained. There is no check that exclusions or missingness were balanced across arms.

**Response.** The reviewer asks for a sensitivity analysis without weights, since the weights' purpose (assignment vs attrition) is unclear. Re-running H1 unweighted shows whether the arm estimates depend on the weighting. Added H1a, a robustness re-estimation of H1: re-fit without inverse probability weights (`{"estimator": {"kind": "lin", "robust": "HC2", "cluster": null, "weights": null, "covariates": ["media_trust", "pk_score", "ai_scale", "political_interest"], "continuous": ["media_trust", "pk_score", "ai_scale", "political_interest"]}}`).

**Result.** H1: +0.010 (SE 0.007, p = 0.132, N = 2030). H1a: +0.012 (SE 0.004, p = 0.004, N = 2030).

## Second reviewer pass

Mostly consistent reporting of arm estimates, but the report leans on uncorrected borderline findings, contains a pooled-vs-arm inconsistency, hides a large robustness sensitivity, and is truncated.

Remaining issues:

- **high** R1 — H1 / Abstract / Key findings: Headline arm effects (Automated Flagging, Guide, Mindfulness) are presented as findings across 11 arms x 4 outcomes with no multiplicity correction; the Guide (p=0.043) and Mindfulness (p=0.032) would not survive any correction. The abstract states them without hedging in the sentence itself.
- **high** R2 — H1a robustness: The unweighted refit (H1a) shows different estimates (e.g. Flagging +0.008 vs -0.010, Guide +0.004 vs +0.047), implying results are sensitive to IPW, yet the report never discusses it.
- **high** R3 — Design and data: Registration came after some data were collected, which is a deviation. It is mentioned only in passing and the tags list no differences. How many responses preceded registration, and whether arms/outcomes were chosen after seeing the data, is not stated.
- **medium** R4 — H1 / Key findings: The Mindfulness arm's mean_arm (0.696) equals its control-adjacent value, yet the estimate is -0.039 with control mean 0.693; the arm means in the summary table don't match the estimates (e.g. Guide mean 0.699 vs +0.047). Adjusted and raw quantities are mixed and unexplained.
- **medium** R5 — H5: The exploratory H5 prose reports pooled p<0.001 and gains in specific arms, but H1 total accuracy is flat. The AI-detection gain is likely offset by a drop in authentic-content accuracy, suggesting a response bias (more 'AI' answers) rather than better discernment. The report does not say so.
- **medium** R6 — Abstract / H2: The pooled attitude effect (-0.11, p=0.026) is described as a finding while the arm effects are inconsistent and the only significant arm is Breathing Exercise. SEs vary oddly across arms (0.116 to 0.280), and Nudge with n=331 has SE 0.276.
- **low** R7 — H1 text: The claim 'other eight arms within about ±2 points' is false: Nudge is +2.0 and Flagging -1.0, which is fine, but Infographic 2 and others are within range; Provenance/Breathing at 1.5 OK. Pooled CI also uses an approximate SE with a shared control.
- **low** R8 — H6: The H6 section is truncated, with an empty 'Details' block and no table.
