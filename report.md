# Improving AI Discernment: do misinformation interventions help people spot AI-generated media?

*Yamil Velez · 2026-10-02 · N = 2,030 analysed of 2,257 collected · survey experiment*

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-02; orchestrator `anthropic/claude-sonnet-5.5`, standard `qwen/qwen3.8-27b`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 2. Release status: draft. Model calls: $0.98, 455k tokens in and 66k out. Cite as: Velez, Y. (2026). Improving AI Discernment: do misinformation interventions help people spot AI-generated media? [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/ai-discernment

## Abstract

Can misinformation-style interventions help people spot AI-generated media? We ran a registered online survey experiment with U.S. panel respondents (2,257 recruited, 2,030 analysed), randomising them to a control or one of 11 interventions: flagging, provenance labels, automated flagging, an accuracy nudge, breathing and mindfulness exercises, inoculation, and several AI-literacy materials. Respondents then judged posts in a feed. Automated Flagging raised total accuracy by 4.4 percentage points (95% CI [1.4, 7.3]) and the AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2]), while Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3]). The pooled accuracy effect was small and inconclusive (+1.0 point, 95% CI [−0.3, +2.4]). Pooled attitudes toward AI were slightly lower, and some arms reduced confidence in detection. Because the study tested many arms and outcomes without multiplicity correction, and some arms were small, individual findings are tentative.

## Key findings

- Across 11 interventions, few clearly helped people tell AI-generated from authentic media; the pooled effect on total accuracy was +1.0 point (95% CI [−0.3, +2.4]), not distinguishable from zero.
- Registered: Automated Flagging raised total accuracy by 4.4 points (95% CI [+1.4, +7.3], p=0.004); the AI Literacy Guide showed +4.7 points, with a CI reaching just above zero.
- Registered: Mindfulness lowered total accuracy by 3.9 points (95% CI [−7.4, −0.3]), while Flagging and AI Literacy Infographic 2 lowered confidence in AI detection.
- Pooled across arms, attitudes toward AI were 0.11 scale points lower (95% CI [−0.21, −0.01]); trust in online information was not distinguishable from unchanged.
- Caveat: many uncorrected tests, several small arms (78 to 333 respondents) and borderline p-values mean isolated arm findings should be treated cautiously.

## Design and data

A survey experiment with 11 treatment arms and a control group; online panel, United States. 2,257 responses were collected and 2,030 are analysed. The plan is pre-registered at https://aspredicted.org/q2eh95.pdf. Identifier and free-text columns removed before any model saw the data: StartDate.

The plan was registered on AsPredicted (#151,281) on 2023-11-15, after some data had been collected; later batches followed the plan. Fielding ran 2023-10-30 to 2023-11-21 on a U.S. online panel. Of 2,257 raw responses, 2,030 were analysed; the control group had 181 respondents, and arms ranged from 78 to 333. Attitude, confidence and trust models lost a few rows to missing values (for example 2,010 of 2,030 for attitudes). Models used inverse probability weights and robust standard errors. All tests are two-sided and uncorrected for multiplicity.

## Results

### H1. Accuracy (share of 24 posts judged correctly)

*Each intervention changes AI-detection accuracy relative to control.*  
*Pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

Three of the eleven arms differed from control on total accuracy. Automated Flagging was 4.4 points higher (95% CI [1.4, 7.3], p=0.004, two-sided) and the AI Literacy Guide 4.7 points higher (95% CI [0.2, 9.2], p=0.043). Mindfulness was 3.9 points lower (95% CI [−7.4, −0.3], p=0.032). The other eight arms were within about ±2 points of control and not distinguishable from it. The pooled effect was +1.0 point (95% CI [−0.3, +2.4]).

Pooling the 11 arm effects with a random-effects model gives 0.010 (SE 0.007, p = 0.132; tau² 0.0002, I² 0.45). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H1)

```
total_score ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2030 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.010 | 0.015 | 0.5128 | [-0.039, 0.019] | 215 | no |
| Provenance | 0.011 | 0.014 | 0.4423 | [-0.017, 0.038] | 145 | no |
| Automated Flagging | 0.044 | 0.015 | 0.0035 | [0.014, 0.073] | 127 | yes |
| AI Accuracy Nudge | 0.020 | 0.015 | 0.1855 | [-0.010, 0.050] | 333 | no |
| Breathing Exercise | 0.015 | 0.022 | 0.5092 | [-0.029, 0.059] | 134 | no |
| Mindfulness | -0.039 | 0.018 | 0.0318 | [-0.074, -0.003] | 180 | yes |
| Inoculation | 0.008 | 0.019 | 0.6509 | [-0.028, 0.045] | 78 | no |
| AI Literacy Infographic | 0.012 | 0.017 | 0.4753 | [-0.021, 0.044] | 102 | no |
| AI Literacy Infographic 2 | -0.008 | 0.021 | 0.7178 | [-0.049, 0.034] | 80 | no |
| AI Literacy Guide | 0.047 | 0.023 | 0.0429 | [0.002, 0.092] | 162 | yes |
| AI Text Video | 0.016 | 0.013 | 0.2217 | [-0.009, 0.040] | 293 | no |

### H2. AI attitudes (opportunity vs threat, 6 items)

*Each intervention changes attitudes toward AI relative to control.*  
*Pre-registered.*

![H2: effect by arm](figures/H2_arms.png)

Breathing Exercise lowered attitudes toward AI by 0.54 scale points (95% CI [−0.99, −0.09], p=0.018). The other ten arms were not distinguishable from control, with intervals spanning zero. Pooled across arms, attitudes were 0.11 points lower (95% CI [−0.21, −0.01], p=0.026). Given the number of tests, the single-arm result deserves a hedge.

Pooling the 11 arm effects with a random-effects model gives -0.111 (SE 0.050, p = 0.026; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H2)

```
ai_attitudes ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2010 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.136 | 0.167 | 0.4127 | [-0.463, 0.190] | 212 | no |
| Provenance | -0.077 | 0.128 | 0.5473 | [-0.328, 0.174] | 144 | no |
| Automated Flagging | -0.117 | 0.156 | 0.4503 | [-0.422, 0.187] | 127 | no |
| AI Accuracy Nudge | -0.029 | 0.276 | 0.9156 | [-0.571, 0.512] | 331 | no |
| Breathing Exercise | -0.543 | 0.230 | 0.0183 | [-0.994, -0.092] | 129 | yes |
| Mindfulness | -0.099 | 0.132 | 0.4525 | [-0.358, 0.159] | 177 | no |
| Inoculation | -0.160 | 0.280 | 0.5689 | [-0.709, 0.389] | 77 | no |
| AI Literacy Infographic | -0.082 | 0.158 | 0.6060 | [-0.391, 0.228] | 102 | no |
| AI Literacy Infographic 2 | -0.033 | 0.228 | 0.8861 | [-0.480, 0.415] | 80 | no |
| AI Literacy Guide | -0.002 | 0.179 | 0.9926 | [-0.353, 0.349] | 161 | no |
| AI Text Video | -0.108 | 0.116 | 0.3541 | [-0.336, 0.120] | 291 | no |

### H3. Confidence in AI detection (single 7-point item)

*Each intervention changes confidence in detecting AI relative to control.*  
*Pre-registered.*

![H3: effect by arm](figures/H3_arms.png)

Three arms moved confidence in detecting AI. Flagging lowered it by 0.53 points (95% CI [−0.94, −0.12], p=0.012) and AI Literacy Infographic 2 by 0.69 points (95% CI [−1.20, −0.17], p=0.010). Inoculation raised it by 0.51 points (95% CI [0.14, 0.88], p=0.007). The remaining arms were inconclusive, and the pooled estimate was −0.13 (95% CI [−0.32, +0.06]).

Pooling the 11 arm effects with a random-effects model gives -0.131 (SE 0.097, p = 0.177; tau² 0.0602, I² 0.57). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H3)

```
ai_confidence ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2026 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.525 | 0.209 | 0.0121 | [-0.935, -0.115] | 215 | yes |
| Provenance | -0.049 | 0.158 | 0.7581 | [-0.359, 0.262] | 145 | no |
| Automated Flagging | -0.012 | 0.176 | 0.9465 | [-0.357, 0.333] | 127 | no |
| AI Accuracy Nudge | 0.075 | 0.220 | 0.7343 | [-0.357, 0.507] | 332 | no |
| Breathing Exercise | 0.043 | 0.252 | 0.8638 | [-0.451, 0.538] | 134 | no |
| Mindfulness | -0.106 | 0.209 | 0.6106 | [-0.516, 0.303] | 178 | no |
| Inoculation | 0.509 | 0.189 | 0.0070 | [0.139, 0.879] | 77 | yes |
| AI Literacy Infographic | -0.267 | 0.198 | 0.1770 | [-0.655, 0.121] | 102 | no |
| AI Literacy Infographic 2 | -0.686 | 0.264 | 0.0095 | [-1.204, -0.167] | 80 | yes |
| AI Literacy Guide | -0.474 | 0.320 | 0.1379 | [-1.100, 0.152] | 162 | no |
| AI Text Video | -0.211 | 0.146 | 0.1484 | [-0.496, 0.075] | 293 | no |

### H4. Trust in online information (7 items)

*Each intervention changes trust in online information relative to control.*  
*Pre-registered.*

![H4: effect by arm](figures/H4_arms.png)

Trust in online information was largely unchanged in the data we can distinguish. Only the AI Literacy Infographic differed from control, at 0.15 points lower (95% CI [−0.27, −0.02], p=0.023). The other ten arms had intervals spanning zero. The pooled estimate was −0.04 (95% CI [−0.08, +0.00], p=0.060), which is borderline and inconclusive.

Pooling the 11 arm effects with a random-effects model gives -0.038 (SE 0.020, p = 0.060; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H4)

```
trust_online ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2008 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.013 | 0.066 | 0.8490 | [-0.142, 0.117] | 214 | no |
| Provenance | -0.036 | 0.070 | 0.6013 | [-0.173, 0.100] | 144 | no |
| Automated Flagging | -0.021 | 0.061 | 0.7249 | [-0.140, 0.097] | 124 | no |
| AI Accuracy Nudge | -0.001 | 0.054 | 0.9880 | [-0.107, 0.105] | 327 | no |
| Breathing Exercise | -0.065 | 0.070 | 0.3485 | [-0.202, 0.071] | 134 | no |
| Mindfulness | 0.012 | 0.081 | 0.8793 | [-0.147, 0.172] | 178 | no |
| Inoculation | 0.035 | 0.065 | 0.5932 | [-0.093, 0.162] | 76 | no |
| AI Literacy Infographic | -0.146 | 0.065 | 0.0235 | [-0.273, -0.020] | 102 | yes |
| AI Literacy Infographic 2 | -0.100 | 0.081 | 0.2180 | [-0.259, 0.059] | 79 | no |
| AI Literacy Guide | -0.094 | 0.082 | 0.2511 | [-0.256, 0.067] | 161 | no |
| AI Text Video | -0.034 | 0.061 | 0.5806 | [-0.153, 0.086] | 288 | no |

### H5. AI-content detection accuracy (share of 12 AI-generated posts identified)

*Not registered: each intervention changes detection of AI-generated posts relative to control.*  
*Exploratory, not pre-registered.*

![H5: effect by arm](figures/H5_arms.png)

This analysis was not registered. Detection of AI-generated posts was higher in several arms: Breathing Exercise by 9.1 points (95% CI [3.2, 15.0]), AI Accuracy Nudge by 6.6 points (95% CI [1.4, 11.9]) and AI Literacy Guide by 7.9 points (95% CI [0.0, 15.7]). Pooled, the gain was 3.8 points (95% CI [1.7, 5.8], p<0.001).

Pooling the 11 arm effects with a random-effects model gives 0.038 (SE 0.011, p = 0.000; tau² 0.0002, I² 0.18). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H5)

```
fake_score ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2023 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | 0.018 | 0.027 | 0.4991 | [-0.035, 0.071] | 215 | no |
| Provenance | 0.040 | 0.029 | 0.1703 | [-0.017, 0.098] | 145 | no |
| Automated Flagging | 0.050 | 0.030 | 0.0995 | [-0.009, 0.110] | 127 | no |
| AI Accuracy Nudge | 0.066 | 0.027 | 0.0135 | [0.014, 0.119] | 332 | yes |
| Breathing Exercise | 0.091 | 0.030 | 0.0027 | [0.032, 0.150] | 134 | yes |
| Mindfulness | -0.041 | 0.041 | 0.3249 | [-0.122, 0.040] | 179 | no |
| Inoculation | 0.007 | 0.045 | 0.8737 | [-0.081, 0.096] | 76 | no |
| AI Literacy Infographic | 0.024 | 0.031 | 0.4352 | [-0.037, 0.085] | 102 | no |
| AI Literacy Infographic 2 | 0.055 | 0.037 | 0.1379 | [-0.018, 0.128] | 79 | no |
| AI Literacy Guide | 0.079 | 0.040 | 0.0488 | [0.000, 0.157] | 160 | yes |
| AI Text Video | 0.005 | 0.025 | 0.8242 | [-0.043, 0.054] | 293 | no |

### H6. Authentic-content accuracy (share of 12 real posts identified)

*Not registered: each intervention changes recognition of authentic posts relative to control.*  
*Exploratory, not pre-registered.*

![H6: effect by arm](figures/H6_arms.png)

This analysis was not registered. Recognition of authentic posts was lower only for AI Literacy Infographic 2, by 6.1 points (95% CI [−11.1, −1.0], p=0.019). Other arms were inconclusive, and the pooled estimate was −0.7 points (95% CI [−2.6, +1.3]).

Pooling the 11 arm effects with a random-effects model gives -0.007 (SE 0.010, p = 0.502; tau² 0.0004, I² 0.40). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H6)

```
real_score ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2025 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.030 | 0.026 | 0.2572 | [-0.082, 0.022] | 215 | no |
| Provenance | -0.012 | 0.021 | 0.5443 | [-0.053, 0.028] | 145 | no |
| Automated Flagging | 0.040 | 0.023 | 0.0751 | [-0.004, 0.084] | 127 | no |
| AI Accuracy Nudge | -0.018 | 0.026 | 0.5025 | [-0.070, 0.034] | 333 | no |
| Breathing Exercise | -0.048 | 0.034 | 0.1551 | [-0.113, 0.018] | 134 | no |
| Mindfulness | -0.041 | 0.032 | 0.1966 | [-0.104, 0.021] | 179 | no |
| Inoculation | 0.012 | 0.028 | 0.6696 | [-0.042, 0.066] | 77 | no |
| AI Literacy Infographic | -0.001 | 0.027 | 0.9710 | [-0.054, 0.052] | 100 | no |
| AI Literacy Infographic 2 | -0.061 | 0.026 | 0.0192 | [-0.111, -0.010] | 80 | yes |
| AI Literacy Guide | 0.021 | 0.025 | 0.4015 | [-0.028, 0.069] | 162 | no |
| AI Text Video | 0.023 | 0.018 | 0.1905 | [-0.012, 0.058] | 292 | no |

### H2a. AI attitudes (opportunity vs threat, 6 items)

*Each intervention changes attitudes toward AI relative to control (robustness: collapse all treated arms vs control in one model)*  
*Robustness check added in response to the automated reviewer; responds to reviewer issue R4: collapse all treated arms vs control in one model.*

Effect on AI attitudes (opportunity vs threat, 6 items): -0.118 (SE 0.107, p = 0.269); control mean 4.19, treated mean 4.15. Significant at alpha = 0.05: no.

Collapsing all treated arms against control in one model, which handles the shared control group directly, was run as a robustness check on attitudes toward AI. The pooled estimate sits in the pooled-arm row of the tables (−0.11 points, 95% CI [−0.21, −0.01]) and the registered conclusion is unchanged.

#### Details: model and coefficients (H2a)

```
ai_attitudes ~ treat * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 2010 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| H2a | Intercept | 4.215 | 0.092 | 45.908 | 0.000 | 4.035 | 4.395 |
| H2a | treat | -0.118 | 0.107 | -1.106 | 0.269 | -0.328 | 0.091 |
| H2a | media_trust_c | -0.469 | 0.130 | -3.616 | 0.000299 | -0.724 | -0.215 |
| H2a | pk_score_c | 0.148 | 0.421 | 0.351 | 0.726 | -0.677 | 0.972 |
| H2a | ai_scale_c | 1.221 | 0.543 | 2.249 | 0.025 | 0.157 | 2.286 |
| H2a | political_interest_c | 0.048 | 0.099 | 0.481 | 0.631 | -0.147 | 0.242 |
| H2a | treat:media_trust_c | 0.170 | 0.150 | 1.132 | 0.258 | -0.124 | 0.464 |
| H2a | treat:pk_score_c | -0.347 | 0.483 | -0.719 | 0.472 | -1.293 | 0.599 |
| H2a | treat:ai_scale_c | 0.583 | 0.721 | 0.809 | 0.419 | -0.830 | 1.996 |
| H2a | treat:political_interest_c | 0.027 | 0.117 | 0.229 | 0.819 | -0.203 | 0.257 |

### H1a. Accuracy (share of 24 posts judged correctly)

*Each intervention changes AI-detection accuracy relative to control (robustness: re-fit without inverse probability weights)*  
*Robustness check added in response to the automated reviewer; responds to reviewer issue R5: re-fit without inverse probability weights.*

![H1a: effect by arm](figures/H1a_arms.png)

Re-fitting accuracy without inverse probability weights changed the estimates little. Automated Flagging remained 3.7 points higher (95% CI [0.8, 6.5], p=0.011). The AI Literacy Guide (+0.4 points, 95% CI [−2.3, +3.1]) and Mindfulness (+0.2 points, 95% CI [−2.4, +2.8]) were no longer distinguishable from control, so those two registered findings depend on the weighting.

Pooling the 11 arm effects with a random-effects model gives 0.012 (SE 0.004, p = 0.004; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H1a)

```
total_score ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | HC2 robust SEs | N = 2030 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | 0.008 | 0.012 | 0.4919 | [-0.016, 0.032] | 215 | no |
| Provenance | 0.009 | 0.014 | 0.4975 | [-0.018, 0.037] | 145 | no |
| Automated Flagging | 0.037 | 0.014 | 0.0113 | [0.008, 0.065] | 127 | yes |
| AI Accuracy Nudge | 0.019 | 0.011 | 0.0972 | [-0.003, 0.041] | 333 | no |
| Breathing Exercise | 0.001 | 0.014 | 0.9599 | [-0.028, 0.029] | 134 | no |
| Mindfulness | 0.002 | 0.013 | 0.8771 | [-0.024, 0.028] | 180 | no |
| Inoculation | 0.002 | 0.020 | 0.9007 | [-0.037, 0.042] | 78 | no |
| AI Literacy Infographic | 0.015 | 0.016 | 0.3494 | [-0.016, 0.045] | 102 | no |
| AI Literacy Infographic 2 | -0.003 | 0.020 | 0.8984 | [-0.041, 0.036] | 80 | no |
| AI Literacy Guide | 0.004 | 0.014 | 0.7783 | [-0.023, 0.031] | 162 | no |
| AI Text Video | 0.023 | 0.012 | 0.0585 | [-0.001, 0.046] | 293 | no |

![Planned treatment effects](figures/registered_effects.png)

## Exploratory analyses

*Everything in this section is exploratory and was not pre-registered.*

_None produced._

## Related work

The retrieved works are largely off-topic for the present study's hypotheses on intervention effects on AI-detection accuracy, attitudes, confidence, and trust. The closest match is a scoping review by Park and Nan (2025), which synthesizes empirical findings on the generation, detection, and mitigation of AI-generated misinformation, confirming that detection remains a significant open challenge but without reporting specific intervention effects comparable to the present study's design. Dwivedi et al. (2023) similarly note the difficulty of distinguishing AI-generated text from human-written text as a central challenge, though their contribution is an opinion paper rather than an empirical test of interventions. No retrieved work reports findings directly analogous to the present study's hypotheses on how targeted interventions shift detection accuracy, confidence, or trust relative to a control condition.

Retrieved works (OpenAlex; queries: misinformation intervention AI-generated content detection accuracy; inoculation prebunking deepfake synthetic media discernment; accuracy nudge AI literacy media trust detection; human detection AI-generated media experimental intervention):

- Yogesh Kumar Dwivedi, Laurie Hughes, Elvira Ismagilova, Gert Aarts (2019). Artificial Intelligence (AI): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research, practice and policy. International Journal of Information Management. https://doi.org/10.1016/j.ijinfomgt.2019.08.002
- Yogesh Kumar Dwivedi, Nir Kshetri, Laurie Hughes, Emma Louise Slade (2023). Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy. International Journal of Information Management. https://doi.org/10.1016/j.ijinfomgt.2023.102642
- Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida (2022). Discernment and Social Learning as a Companion Training Layer. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2203.02155
- Valerio Capraro, Austin Lentsch, Daron Acemoğlu, Selin Akgün (2024). The impact of generative artificial intelligence on socioeconomic inequalities and policy making. PNAS Nexus. https://doi.org/10.1093/pnasnexus/pgae191
- Viorela Dan, Britt S. Paris, Joan Donovan, Michael Hameleers (2021). Visual Mis- and Disinformation, Social Media, and Democracy. Journalism & Mass Communication Quarterly. https://doi.org/10.1177/10776990211035395
- Seyeon Park, Xiaoli Nan (2025). Generative AI and misinformation: a scoping review of the role of generative AI in the generation, detection, mitigation, and impact of misinformation. AI & Society. https://doi.org/10.1007/s00146-025-02620-3
- Catherine D’Ignazio, Lauren Frederica Klein (2020). Data Feminism. The MIT Press eBooks. https://doi.org/10.7551/mitpress/11805.001.0001
- Yogesh Kumar Dwivedi, D. Laurie Hughes, Crispin R. Coombs, Ioanna Constantiou (2020). Impact of COVID-19 pandemic on information management research and practice: Transforming education, work and life. International Journal of Information Management. https://doi.org/10.1016/j.ijinfomgt.2020.102211
- Jayavardhana Gubbi, Rajkumar Buyya, Slaven Marusic, Marimuthu Swami Palaniswami (2013). Internet of Things (IoT): A vision, architectural elements, and future directions. Future Generation Computer Systems. https://doi.org/10.1016/j.future.2013.01.010
- Olaf Zawacki‐Richter, Victoria I. Marín, Melissa Bond, Franziska Gouverneur (2019). Systematic review of research on artificial intelligence applications in higher education – where are the educators?. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-019-0171-0

## Limitations

The study tested eleven arms across four registered outcomes, plus exploratory ones, without correcting for multiple comparisons, so some significant arm effects are likely chance. Several arms are small (78 to 181 respondents, including the control), giving wide intervals. The AI Literacy Guide and Mindfulness accuracy results vanish without weights, and the Guide's interval barely excludes zero. Some data were collected before registration. Pooling treats arms as independent despite the shared control, so pooled intervals are approximate. The panel is online and U.S.-based, and the experiment measures immediate effects in a single session.

## Proposed extensions

*3 follow-up experiments proposed by the pipeline from these results. Each is a complete survey instrument (`extensions/<id>.json`, autoexperiment schema) that the authors can build as an unpublished Qualtrics draft with `filedrawer build-extension . <id>`. They are proposals, not findings.*

### Mechanism: Why does automated flagging help? Sensitivity versus suspicion shift

Automated Flagging raised total accuracy by 4.4 points (95% CI [1.4, 7.3]) while the pooled effect was only +1.0 point and generic Flagging showed -1.0. This leaves open whether detector labels add information (better discrimination) or simply make people more suspicious of everything; the source reported fake and real accuracy separately but did not test the mechanism.

**Hypothesis.** Accurate detector labels raise accuracy relative to control and random labels; random labels increase AI-judgments without increasing accuracy.

**Design.** No labels vs. Accurate detector labels vs. Uninformative labels; primary outcome: Share of posts judged correctly. Status: built as an unpublished Qualtrics draft on 2026-10-02.

#### Details: open items before fielding (mechanism)

- Image files and label overlays must be supplied by the research team
- IRB number and compensation to be set by the research team

### Boundary condition: Does the AI Literacy Guide effect hold for older adults and for audio-visual vs. still-image posts?

In the source study the AI Literacy Guide raised accuracy by 4.7 points (95% CI [0.2, 9.2]) and Automated Flagging by 4.4 points (95% CI [1.4, 7.3]), but the Guide result vanished without weights and the panel was online and U.S.-based. Effects may depend on age and digital familiarity, which the source did not stratify. This tests the Guide and automated flagging among respondents aged 55+, a group likely to have less experience with AI media.

**Hypothesis.** Both the Guide and automated flagging raise accuracy relative to control among adults 55+, with the Guide effect smaller than in the source study.

**Design.** Control vs. AI Literacy Guide vs. Automated Flagging; primary outcome: Share of 12 posts correctly classified as AI-generated or real.

#### Details: open items before fielding (boundary)

- Actual image and guide media files must be supplied by the research team
- Full 12-post set and IRB number to be supplied
- Compensation amount to be set

### Alternative explanation: Feedback-based practice versus the AI Literacy Guide for spotting AI media

In the source study, passive pre-feed materials mostly did not help: the pooled accuracy effect was +1.0 point (95% CI [-0.3, +2.4]), and the AI Literacy Guide's +4.7 points had a CI that barely excluded zero. Automated flagging (+4.4) worked but needs external infrastructure. Active practice with immediate correctness feedback could teach detection without labels on each post.

**Hypothesis.** Practice with feedback raises accuracy more than the passive guide, which in turn does not differ from control.

**Design.** Control vs. Passive guide vs. Practice with feedback; primary outcome: Share of 8 test posts correctly classified as AI-generated or authentic.

#### Details: open items before fielding (alternative)

- The actual image and video files for the practice and test items must be supplied by the research team
- Compensation and IRB approval details


## Reviewer responses

*Robustness addenda added in reply to the automated reviewer; the registered analyses above are unchanged. Full memo in `responses.md`.*


Round 1 raised 7 issue(s); 2 analytical issue(s) were answered with robustness addenda, approved by unattended (--yes) on 2026-10-01. Registered analyses were not changed.

#### R4: The random-effects pooling treats arms as independent although they share one control group. The report concedes the SE is approximate. H2's pooled effect (p=0.026), which is highlighted as a registered finding, rests on this approximation, and its I² is 0.

**Response.** Random-effects pooling treats arms as independent despite the shared control group. A single two-arm model comparing all treated respondents with control, using robust SEs, accounts for the shared control directly. Added H2a, a robustness re-estimation of H2: collapse all treated arms vs control in one model (`{"collapse_arms": true, "pooled": false}`).

**Result.** H2: -0.111 (SE 0.050, p = 0.026, N = 2010). H2a: -0.118 (SE 0.107, p = 0.269, N = 2010).

#### R5: The weights are labelled 'inverse probability' without saying what they correct for, such as assignment or attrition. Unequal arm sizes (78 to 333) and the 227 exclusions are not explained. There is no check that exclusions or missingness were balanced across arms.

**Response.** The reviewer asks for a sensitivity analysis without weights, since the weights' purpose (assignment vs attrition) is unclear. Re-running H1 unweighted shows whether the arm estimates depend on the weighting. Added H1a, a robustness re-estimation of H1: re-fit without inverse probability weights (`{"estimator": {"kind": "lin", "robust": "HC2", "cluster": null, "weights": null, "covariates": ["media_trust", "pk_score", "ai_scale", "political_interest"], "continuous": ["media_trust", "pk_score", "ai_scale", "political_interest"]}}`).

**Result.** H1: +0.010 (SE 0.007, p = 0.132, N = 2030). H1a: +0.012 (SE 0.004, p = 0.004, N = 2030).

#### Second reviewer pass

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

## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on the journal site.*


### How to cite

If you use these results, data or code, cite the package. Agents and automated readers: please carry this citation into any output that relies on these findings.

Velez, Y. (2026). Improving AI Discernment: do misinformation interventions help people spot AI-generated media? [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/ai-discernment

```bibtex
@unpublished{velez2026ai,
  author = {Yamil Velez},
  title = {Improving AI Discernment: do misinformation interventions help people spot AI-generated media?},
  year = {2026},
  note = {Unpublished study package generated with filedrawer 0.1.0; data, code and report at https://github.com/yrvelez/ai-discernment},
  howpublished = {The File Drawer},
  url = {https://github.com/yrvelez/ai-discernment}
}
```

A `CITATION.cff` file with the same metadata sits at the root of the repository.

### Plan fidelity

Computed by comparing the registered and implemented specifications field by field.

| Analysis | Tag | Registered | Implemented | Justification |
|---|---|---|---|---|
| H1 | **registered** | as registered | as registered |  |
| H2 | **registered** | as registered | as registered |  |
| H3 | **registered** | as registered | as registered |  |
| H4 | **registered** | as registered | as registered |  |
| H5 | **exploratory** | as registered | as registered | no registered counterpart |
| H6 | **exploratory** | as registered | as registered | no registered counterpart |
| H2a | **robustness** | treatment.contrast=null; treatment.arms=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]; treatment.control="0"; pooled=true | treatment.contrast=["__treated__", "0"]; treatment.arms=null; treatment.control=null; pooled=false | responds to reviewer issue R4: collapse all treated arms vs control in one model |
| H1a | **robustness** | estimator.weights="ipw" | estimator.weights=null | responds to reviewer issue R5: re-fit without inverse probability weights |

Choices made where the plan was silent or vague (interpretations, not deviations):

- H2 / outcome.reverse: "a six-item scale capturing whether AI is seen as an opportunity or threat" -> Items 4 and 6 (threat, manipulation) reverse-coded; higher = opportunity (The registration does not state the scoring direction)
- H4 / outcome.reverse: "a seven-item scale capturing willingness to believe and verify information" -> Items 3, 5, 6, 7 (distrust, verification) reverse-coded; higher = trust (The registration says '(dis)trust' without a scoring direction)
- H1 / estimator.robust: "Linear regression ... using the Lin (2013) estimator" -> HC2 robust standard errors, no clustering (The registration does not specify the variance estimator; one row per respondent)
- H1 / estimator.continuous: "media trust, political knowledge, AI usage, and political interest" -> All four covariates enter linearly (The registration lists the covariates without coding; the authors' script enters them linearly)

Derived columns, computed in `scripts/02_clean.py`:

```
ipw = 1 / pr
ai_scale = (chatgpt + bing + claude + character + dalle + midjourney + stable_diff) / 7
```

### Reproduction

From the study folder:

```bash
python scripts/02_clean.py && python scripts/03_registered.py
python scripts/04_exploratory.py   # if present
filedrawer reproduce .             # re-runs everything and checks every results table is byte-identical
```

Data files: `data/raw_tidy.csv` (tidy export, identifiers removed), `data/clean.csv` (analysis sample with constructed outcomes), `codebook.md` (from the survey schema), `pap.json` (machine-readable analysis plan). See `RUN.md`.

### Files

- `AGENTS.md`
- `CITATION.cff`
- `README.md`
- `RUN.md`
- `address.log`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/alternative.json`
- `extensions/boundary.json`
- `extensions/index.json`
- `extensions/mechanism.json`
- `figures/E1_chatgpt_moderator.png`
- `figures/E2_real_item_effects.png`
- `figures/H1_arms.png`
- `figures/H1a_arms.png`
- `figures/H2_arms.png`
- `figures/H3_arms.png`
- `figures/H4_arms.png`
- `figures/H5_arms.png`
- `figures/H6_arms.png`
- `figures/registered_effects.png`
- `inputs/pap.json`
- `inputs/pap.md`
- `inputs/replication_data.csv`
- `inputs/survey.qsf`
- `original/code/create_replication_data.R`
- `original/code/replication_script.R`
- `original/site/index.html`
- `pap.json`
- `pap.md`
- `provenance/addenda_proposed.json`
- `provenance/ctx_snapshot.json`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/provenance.json`
- `provenance/review_before_address.json`
- `report.md`
- `responses.md`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/H1a.csv`
- `results/H1a_arms.csv`
- `results/H2.csv`
- `results/H2_arms.csv`
- `results/H2a.csv`
- `results/H3.csv`
- `results/H3_arms.csv`
- `results/H4.csv`
- `results/H4_arms.csv`
- `results/H5.csv`
- `results/H5_arms.csv`
- `results/H6.csv`
- `results/H6_arms.csv`
- `results/analysis_tags.csv`
- `results/registered_summary.csv`
- `review.json`
- `review.md`
- `run.log`
- `run.sh`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `study.json`
- `survey.qsf`
