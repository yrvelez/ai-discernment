# Improving AI Discernment: do misinformation interventions help people spot AI-generated media?

*Yamil Velez · 2026-10-03 · N = 2,030 analysed of 2,257 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: round 2 · 8/12 claims supported](figures/badges/review.svg) [![plan: pre-registered #151,281](figures/badges/registration.svg)](https://aspredicted.org/q2eh95.pdf) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $1.32](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-03; orchestrator `anthropic/claude-sonnet-5.5`, standard `qwen/qwen3.8-27b`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 2. Release status: draft. Model calls: $1.32, 495k tokens in and 94k out. Cite as: Velez, Y. (2026). Improving AI Discernment: do misinformation interventions help people spot AI-generated media? [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/ai-discernment

<!-- fd:section id=abstract -->
## Abstract

Can common misinformation interventions help people tell AI-generated media from authentic media? We ran a registered online survey experiment with a US panel (fielded October to November 2023; 2,257 respondents, 2,030 analysed), randomising respondents to a control or one of 11 interventions, including flagging, provenance labels, an accuracy nudge, calming exercises, inoculation and AI literacy materials. Pooled across arms, total accuracy was 1.0 point higher than control (95% CI [−0.3, 2.4]). In uncorrected tests, Automated Flagging nominally raised accuracy by 4.4 points (95% CI [1.4, 7.3]) and the AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2]); Mindfulness nominally lowered it by 3.9 points (95% CI [−7.4, −0.3]). When low-knowledge respondents were excluded, only Automated Flagging remained (p=0.044). Because 44 registered tests were uncorrected and some arms are small, findings should be treated cautiously.

<!-- fd:section id=findings -->
## Key findings

- Interventions did not clearly improve people's ability to spot AI-generated media: pooled across 11 arms, total accuracy was 1.0 point higher (95% CI [−0.3, +2.4]), not distinguishable from zero.
- Registered but nominal and uncorrected: Automated Flagging had 4.4 points higher total accuracy (95% CI [1.4, 7.3], p=0.004); it also held when low-knowledge respondents were excluded (p=0.044).
- The AI Literacy Guide (+4.7 points) and Mindfulness (−3.9 points, 95% CI [−7.4, −0.3]) were nominal total accuracy effects that did not hold when low-knowledge respondents were excluded.
- Pooled across arms, attitudes toward AI were 0.11 scale points lower (95% CI [−0.21, −0.01]); this is a small shift.
- Caveat: 44 registered tests were run without multiplicity correction, several arms are small, and results near the threshold may be chance.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 11 arms and a control group; online panel, United States. 2,257 responses were collected and 2,030 are analysed. The plan is pre-registered at https://aspredicted.org/q2eh95.pdf. Identifier and free-text columns removed before any model saw the data: none.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in United States (N = 2,030 analysed). Respondents are randomly assigned to 12 arms: Flagging, Provenance, Automated Flagging, AI Accuracy Nudge, Breathing Exercise, Mindfulness, Inoculation, AI Literacy Infographic, AI Literacy Infographic 2, AI Literacy Guide, AI Text Video, against the control group Control. Flagging: Posts in the feed are flagged as potentially AI-generated. Provenance: Posts carry information about the content's source and origin (provenance). Automated Flagging: Posts carry machine-learning-based AI-detection labels (automated flagging). AI Accuracy Nudge: Before the feed, an interactive task asks 'Is this image AI-generated?' (accuracy nudge). Breathing Exercise: Before the feed, a box-breathing exercise to reduce emotional reactivity. Mindfulness: Before the feed, a short mindfulness exercise. Inoculation: Before the feed, an inoculation message pre-exposing the respondent to manipulation techniques used in AI-generated media. AI Literacy Infographic: Before the feed, an infographic on how to identify AI-generated content. AI Literacy Infographic 2: Before the feed, an alternative infographic on how to identify AI-generated content. AI Literacy Guide: Before the feed, a comprehensive guide with examples of AI artifacts in images and videos. AI Text Video: Before the feed, an educational video about AI-generated text. Outcomes: Accuracy (share of 24 posts judged correctly), AI attitudes (opportunity vs threat, 6 items), Confidence in AI detection (single 7-point item), Trust in online information (7 items).


The plan was registered on AsPredicted (#151,281, 2023-11-15), but some data had been collected already; batches 3-4 followed the plan, and the tables do not say which arms or batches came earlier. Of 2,257 raw respondents, 2,030 were analysed. Arms ranged from 78 to 333 respondents; the control group is the comparison for every contrast (control mean accuracy 0.693). Small losses came from missing outcome values, for example 212 of 215 in the Flagging arm for attitudes. Inverse-probability weights, exclusion rules and attrition by arm are not documented in the material available here. The timing of the political-knowledge score relative to treatment is not stated. All p-values are two-sided, with no multiplicity correction.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=registered outcome=total_score -->
### H1. Accuracy (share of 24 posts judged correctly)

*Each intervention changes AI-detection accuracy relative to control.*  
*Pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

Three arms differed from control in uncorrected tests. Automated Flagging was 4.4 points higher (95% CI [1.4, 7.3], p=0.004, two-sided) and the AI Literacy Guide 4.7 points higher (95% CI [0.2, 9.2], p=0.043). Mindfulness was 3.9 points lower (95% CI [−7.4, −0.3], p=0.032). Treat all three as nominal given 44 uncorrected tests. The other eight arms were within about ±2 points of control and not distinguishable from it. The pooled estimate was 1.0 point (95% CI [−0.3, 2.4]).

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

<!-- fd:hyp id=H2 tag=registered outcome=ai_attitudes -->
### H2. AI attitudes (opportunity vs threat, 6 items)

*Each intervention changes attitudes toward AI relative to control.*  
*Pre-registered.*

![H2: effect by arm](figures/H2_arms.png)

Attitudes toward AI were 0.54 scale points lower in the Breathing Exercise arm (95% CI [−0.99, −0.09], p=0.018). It was the only one of eleven arms to differ, so it looks isolated and exploratory in character. Without covariates (H2a) the estimate was −0.63 (p=0.011). The other ten arms were within about 0.16 points of control, with intervals spanning zero. Pooled attitudes were 0.11 points lower (95% CI [−0.21, −0.01], p=0.026).

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

<!-- fd:hyp id=H3 tag=registered outcome=ai_confidence -->
### H3. Confidence in AI detection (single 7-point item)

*Each intervention changes confidence in detecting AI relative to control.*  
*Pre-registered.*

![H3: effect by arm](figures/H3_arms.png)

Confidence in detecting AI was lower in two arms: AI Literacy Infographic 2 by 0.69 points (95% CI [−1.20, −0.17], p=0.010) and Flagging by 0.53 points (95% CI [−0.94, −0.12], p=0.012). Inoculation raised confidence by 0.51 points (95% CI [0.14, 0.88], p=0.007). The other eight arms were not distinguishable from control. The pooled estimate was −0.13 (95% CI [−0.32, 0.06]), inconclusive.

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

<!-- fd:hyp id=H4 tag=registered outcome=trust_online -->
### H4. Trust in online information (7 items)

*Each intervention changes trust in online information relative to control.*  
*Pre-registered.*

![H4: effect by arm](figures/H4_arms.png)

Trust in online information was lower under the AI Literacy Infographic by 0.15 points (95% CI [−0.27, −0.02], p=0.023). The other ten arms were within about ±0.1 points of control, with intervals spanning zero. The pooled estimate was −0.04 (95% CI [−0.08, 0.00], p=0.060), which is inconclusive. A single nominal result among eleven tests is weak evidence.

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

<!-- fd:hyp id=H1a tag=robustness outcome=total_score -->
### H1a. Accuracy (share of 24 posts judged correctly)

*Each intervention changes AI-detection accuracy relative to control (robustness: exclude low political-knowledge respondents (pk_score<1), full estimates and CIs)*  
*Robustness check added in response to the automated reviewer; responds to reviewer issue R1: exclude low political-knowledge respondents (pk_score<1), full estimates and CIs.*

![H1a: effect by arm](figures/H1a_arms.png)

Excluding respondents with low political-knowledge scores (pk_score<1) left Automated Flagging at 3.6 points (95% CI [0.1, 7.2], p=0.044). The AI Literacy Guide shrank to 2.3 points (95% CI [−3.0, 7.7], p=0.39) and Mindfulness to −3.7 points (95% CI [−8.3, 1.0], p=0.122). Only Automated Flagging holds; the other two are not robust to this exclusion.

Pooling the 11 arm effects with a random-effects model gives 0.009 (SE 0.006, p = 0.135; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H1a)

```
total_score ~ C(arm_code, Treatment(reference='0')) * (media_trust_c + pk_score_c + ai_scale_c + political_interest_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 1417 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.006 | 0.015 | 0.7122 | [-0.036, 0.025] | 155 | no |
| Provenance | -0.000 | 0.018 | 0.9921 | [-0.035, 0.034] | 98 | no |
| Automated Flagging | 0.036 | 0.018 | 0.0438 | [0.001, 0.072] | 82 | yes |
| AI Accuracy Nudge | 0.021 | 0.017 | 0.2167 | [-0.012, 0.055] | 235 | no |
| Breathing Exercise | 0.014 | 0.023 | 0.5465 | [-0.031, 0.059] | 89 | no |
| Mindfulness | -0.037 | 0.024 | 0.1218 | [-0.083, 0.010] | 124 | no |
| Inoculation | 0.004 | 0.022 | 0.8496 | [-0.038, 0.047] | 57 | no |
| AI Literacy Infographic | 0.017 | 0.019 | 0.3595 | [-0.019, 0.053] | 75 | no |
| AI Literacy Infographic 2 | 0.004 | 0.025 | 0.8704 | [-0.046, 0.054] | 58 | no |
| AI Literacy Guide | 0.023 | 0.027 | 0.3923 | [-0.030, 0.077] | 113 | no |
| AI Text Video | 0.009 | 0.015 | 0.5275 | [-0.020, 0.039] | 211 | no |

<!-- fd:hyp id=H2a tag=robustness outcome=ai_attitudes -->
### H2a. AI attitudes (opportunity vs threat, 6 items)

*Each intervention changes attitudes toward AI relative to control (robustness: unadjusted difference in means, no covariates, same weights)*  
*Robustness check added in response to the automated reviewer; responds to reviewer issue R4: unadjusted difference in means, no covariates, same weights.*

![H2a: effect by arm](figures/H2a_arms.png)

Without covariates, the Breathing Exercise estimate was −0.63 scale points (95% CI [−1.12, −0.15], p=0.011), similar to the adjusted −0.54. The other ten arms remained not distinguishable from control. The registered conclusion holds, so the result does not depend on covariate adjustment.

Pooling the 11 arm effects with a random-effects model gives -0.134 (SE 0.054, p = 0.013; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H2a)

```
ai_attitudes ~ C(arm_code, Treatment(reference='0'))
difference in means | weights = ipw | HC2 robust SEs | N = 2010 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Flagging | -0.015 | 0.187 | 0.9376 | [-0.382, 0.352] | 212 | no |
| Provenance | -0.088 | 0.137 | 0.5223 | [-0.356, 0.181] | 144 | no |
| Automated Flagging | -0.213 | 0.162 | 0.1878 | [-0.530, 0.104] | 127 | no |
| AI Accuracy Nudge | -0.088 | 0.237 | 0.7089 | [-0.553, 0.376] | 331 | no |
| Breathing Exercise | -0.633 | 0.249 | 0.0111 | [-1.121, -0.145] | 129 | yes |
| Mindfulness | 0.004 | 0.169 | 0.9815 | [-0.328, 0.336] | 177 | no |
| Inoculation | -0.295 | 0.299 | 0.3247 | [-0.882, 0.292] | 77 | no |
| AI Literacy Infographic | -0.104 | 0.156 | 0.5049 | [-0.409, 0.202] | 102 | no |
| AI Literacy Infographic 2 | 0.001 | 0.250 | 0.9976 | [-0.490, 0.492] | 80 | no |
| AI Literacy Guide | -0.117 | 0.203 | 0.5658 | [-0.515, 0.282] | 161 | no |
| AI Text Video | -0.169 | 0.123 | 0.1670 | [-0.409, 0.071] | 291 | no |

![Planned treatment effects](figures/registered_effects.png)

<!-- fd:section id=exploratory-authors -->
## Exploratory analyses specified by the authors

*Not pre-registered. The authors specified these analyses after seeing the data; they are run by the same deterministic scripts as the registered tests and should be read as hypothesis-generating.*

<!-- fd:hyp id=H5 tag=exploratory outcome=fake_score -->
### H5. AI-content detection accuracy (share of 12 AI-generated posts identified)

*Not registered: each intervention changes detection of AI-generated posts relative to control.*  
*Exploratory, not pre-registered.*

![H5: effect by arm](figures/H5_arms.png)

This outcome was not registered, so these tests are post hoc. Detection of AI-generated posts was higher under the AI Accuracy Nudge by 6.6 points (95% CI [1.4, 11.9], p=0.014), the Breathing Exercise by 9.1 points (95% CI [3.2, 15.0], p=0.003) and the AI Literacy Guide by 7.9 points (95% CI [0.0, 15.7], p=0.049). The other eight arms were not distinguishable from control.

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

<!-- fd:hyp id=H6 tag=exploratory outcome=real_score -->
### H6. Authentic-content accuracy (share of 12 real posts identified)

*Not registered: each intervention changes recognition of authentic posts relative to control.*  
*Exploratory, not pre-registered.*

![H6: effect by arm](figures/H6_arms.png)

This outcome was not registered, so these tests are post hoc. Recognition of authentic posts was lower under AI Literacy Infographic 2 by 6.1 points (95% CI [−11.1, −1.0], p=0.019). The other ten arms were not distinguishable from control. One might speculate that some arms shift how people classify posts, but no discernment or bias measure supports that, so it remains speculation.

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

<!-- fd:section id=exploratory -->
## Further exploratory analyses (proposed by the pipeline)

*Everything in this section is exploratory and was not pre-registered.*

<!-- fd:hyp id=E1 tag=exploratory kind=pipeline -->
### E1. H1 robustness: excluding attention-check failures

Respondents who fail both knowledge questions may not have engaged with the task, so excluding them tests whether registered H1 effects are driven by inattentive respondents. Re-fit the registered H1 model (total_score ~ arm × covariates, IPW, HC2) on the subsample with pk_score >= 1 (n=1417 vs 2030 full); compare arm-level ATEs and SEs side by side.

**Finding.** Excluding 613 attention-check failures (n 2030→1417) eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns; AI Literacy Guide p=0.043→ns), suggesting those effects were concentrated among respondents who also passed the knowledge checks.

![H1 robustness: excluding attention-check failures](figures/E1_h1_no_attention_fail.png)

This unreviewed check, relabelled as a low-knowledge exclusion rather than an attention check, has empty estimate columns, so its claim is unsupported and is withdrawn. The reviewed rerun (H1a) shows Automated Flagging remaining at p=0.044 and the Guide not robust.

#### Details: table (E1)

| arm_code | arm_label | est_full | se_full | p_full | est_excl | se_excl | p_excl | n_full | n_excl |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Flagging |  |  |  |  |  |  | 215 | 155 |
| 2 | Provenance |  |  |  |  |  |  | 145 | 98 |
| 3 | Automated Flagging |  |  |  |  |  |  | 127 | 82 |
| 4 | AI Accuracy Nudge |  |  |  |  |  |  | 333 | 235 |
| 5 | Breathing Exercise |  |  |  |  |  |  | 134 | 89 |
| 6 | Mindfulness |  |  |  |  |  |  | 180 | 124 |
| 7 | Inoculation |  |  |  |  |  |  | 78 | 57 |
| 8 | AI Literacy Infographic |  |  |  |  |  |  | 102 | 75 |
| 9 | AI Literacy Infographic 2 |  |  |  |  |  |  | 80 | 58 |
| 10 | AI Literacy Guide |  |  |  |  |  |  | 162 | 113 |
| 11 | AI Text Video |  |  |  |  |  |  | 293 | 211 |

<!-- fd:hyp id=E2 tag=exploratory kind=pipeline -->
### E2. H1 heterogeneity by prior AI familiarity

Interventions that teach AI detection may work differently for respondents who already know AI tools versus those who do not; this checks whether registered H1 effects are concentrated among low-familiarity respondents. Split sample at the median of ai_scale (0.143); re-fit the registered H1 model separately in each half; compare arm-level ATEs.

**Finding.** No arm reached p<0.05 in either the low-familiarity or high-familiarity subsample, indicating the registered H1 effects (Automated Flagging, AI Literacy Guide) are not concentrated in either familiarity group and likely reflect sampling variability.

![H1 heterogeneity by prior AI familiarity](figures/E2_h1_ai_familiarity.png)

This unreviewed check on AI familiarity has empty estimate and p-value columns and no interaction test, so no conclusion can be drawn from it.

#### Details: table (E2)

| arm_code | arm_label | est_low | se_low | p_low | est_high | se_high | p_high | n_low | n_high |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Flagging |  |  |  |  |  |  | 143 | 72 |
| 2 | Provenance |  |  |  |  |  |  | 90 | 55 |
| 3 | Automated Flagging |  |  |  |  |  |  | 89 | 38 |
| 4 | AI Accuracy Nudge |  |  |  |  |  |  | 219 | 114 |
| 5 | Breathing Exercise |  |  |  |  |  |  | 87 | 47 |
| 6 | Mindfulness |  |  |  |  |  |  | 117 | 63 |
| 7 | Inoculation |  |  |  |  |  |  | 46 | 32 |
| 8 | AI Literacy Infographic |  |  |  |  |  |  | 61 | 41 |
| 9 | AI Literacy Infographic 2 |  |  |  |  |  |  | 55 | 25 |
| 10 | AI Literacy Guide |  |  |  |  |  |  | 101 | 61 |
| 11 | AI Text Video |  |  |  |  |  |  | 191 | 102 |

<!-- fd:hyp id=E3 tag=exploratory kind=pipeline -->
### E3. Placebo: effect of interventions on pre-treatment knowledge (pk_score)

If interventions affect a pre-treatment knowledge score, this would indicate a manipulation or implementation problem; a null result supports the validity of the experimental design. Weighted least squares (IPW, HC2) of pk_score on arm dummies for all 11 treatment arms vs control (n=2030).

**Finding.** No intervention significantly affected pre-treatment knowledge (all p > 0.116, max p = 0.816), confirming the randomisation and that no arm differentially exposed respondents to the knowledge questions.

This unreviewed placebo check on pre-treatment knowledge found min p=0.116 across arms, consistent with balance. No joint test is reported.

#### Details: table (E3)

| arm_code | arm_label | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| 1 | Flagging | 0.029 | 0.043 | 0.509 | 215 |
| 2 | Provenance | -0.021 | 0.035 | 0.541 | 145 |
| 3 | Automated Flagging | -0.021 | 0.034 | 0.540 | 127 |
| 4 | AI Accuracy Nudge | 0.054 | 0.034 | 0.116 | 333 |
| 5 | Breathing Exercise | 0.026 | 0.043 | 0.549 | 134 |
| 6 | Mindfulness | -0.009 | 0.038 | 0.816 | 180 |
| 7 | Inoculation | 0.032 | 0.040 | 0.429 | 78 |
| 8 | AI Literacy Infographic | 0.034 | 0.034 | 0.328 | 102 |
| 9 | AI Literacy Infographic 2 | -0.028 | 0.059 | 0.638 | 80 |
| 10 | AI Literacy Guide | 0.044 | 0.040 | 0.268 | 162 |
| 11 | AI Text Video | 0.030 | 0.027 | 0.272 | 293 |


<!-- fd:section id=related -->
## Related work

Prior findings offer partial, indirect support for the study's hypotheses. Lewandowsky and van der Linden (2021) document that inoculation and prebunking interventions can shift attitudes toward misinformation, providing a basis for expecting effects on attitudes (H2) and trust in online information (H4). Ecker et al. (2022) identify psychological drivers that make misinformation beliefs resistant to correction, suggesting that attitude and trust outcomes may be harder to move than detection accuracy (H1). Capraro et al. (2024) frame generative AI as a new vector for (mis)information, contextualizing why detection of AI-generated posts (H5) and recognition of authentic posts (H6) are relevant outcomes. The retrieved list is thin on work directly addressing human detection of AI-generated text specifically; most supporting evidence is about misinformation more broadly.

A live disagreement concerns the sufficiency of individual-level interventions. Chater and Loewenstein (2022) argue that focusing on individual-level behavioral solutions has led policy astray and that system-level changes are necessary, which contests the premise that the study's individual-level design can produce meaningful effects on any of its outcomes. Ecker et al. (2022) reinforce this skepticism by showing that belief correction is psychologically difficult. The study's controlled intervention design can speak to whether individual-level changes in detection accuracy, confidence, attitudes, or trust are detectable at all, but it cannot adjudicate the broader claim that such changes are insufficient without system-level reform.

Retrieved works (OpenAlex; queries: inoculation theory deepfake detection accuracy; accuracy nudge AI-generated content identification; misinformation intervention backfire effect AI literacy; media literacy intervention null effect synthetic media detection; Lin estimator randomized controlled trial survey intervention effect size):

- Ullrich K. H. Ecker, Stephan Lewandowsky, John Cook, Philipp Schmid (2022). The psychological drivers of misinformation belief and its resistance to correction. Nature Reviews Psychology. https://doi.org/10.1038/s44159-021-00006-y
- Stephan Lewandowsky, Sander van der Linden (2021). Countering Misinformation and Fake News Through Inoculation and Prebunking. European Review of Social Psychology. https://doi.org/10.1080/10463283.2021.1876983
- Esma Aı̈meur, Sabrine Amri, Gilles Brassard (2023). Fake news, disinformation and misinformation in social media: a review. Social Network Analysis and Mining. https://doi.org/10.1007/s13278-023-01028-5
- Natalia Díaz-Rodríguez, Javier Del Ser, Mark Coeckelbergh, Marcos López de Prado (2023). Connecting the dots in trustworthy Artificial Intelligence: From AI principles, ethics, and key requirements to responsible AI systems and regulation. Information Fusion. https://doi.org/10.1016/j.inffus.2023.101896
- Nick Chater, George F. Loewenstein (2022). The i-frame and the s-frame: How focusing on individual-level solutions has led behavioral public policy astray. Behavioral and Brain Sciences. https://doi.org/10.1017/s0140525x22002023
- Valerio Capraro, Austin Lentsch, Daron Acemoğlu, Selin Akgün (2024). The impact of generative artificial intelligence on socioeconomic inequalities and policy making. PNAS Nexus. https://doi.org/10.1093/pnasnexus/pgae191
- A.-W. Chan, Jennifer Tetzlaff, Peter Christian Gøtzsche, Douglas G. Altman (2013). SPIRIT 2013 explanation and elaboration: guidance for protocols of clinical trials. BMJ. https://doi.org/10.1136/bmj.e7586
- Nathan R. Hill, Samuel Fatoba, Jason Lee Oke, Jennifer A. Hirst (2016). Global Prevalence of Chronic Kidney Disease – A Systematic Review and Meta-Analysis. PLoS ONE. https://doi.org/10.1371/journal.pone.0158765
- Goodarz Danaei, Eric L. Ding, Dariush Mozaffarian, Ben Taylor (2009). The Preventable Causes of Death in the United States: Comparative Risk Assessment of Dietary, Lifestyle, and Metabolic Risk Factors. PLoS Medicine. https://doi.org/10.1371/journal.pmed.1000058
- PRISMA-P Group, David Moher, Larissa Shamseer, Mike J Clarke (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. Systematic Reviews. https://doi.org/10.1186/2046-4053-4-1

<!-- fd:section id=limitations -->
## Limitations

Eleven arms across four registered outcomes yield 44 tests with no multiplicity correction, so nominal results near p=0.05 may be chance. Some arms have under 100 respondents, giving wide intervals. Some data were collected before registration. The timing of the knowledge score relative to treatment is unclear, so the low-knowledge exclusion could be post-treatment. Outcomes come from a single online session with a panel sample, so durability is untested. H5 and H6 are post hoc, and the pipeline's exploratory checks are unreviewed. Non-significant arms are inconclusive, not evidence of no effect.

<!-- fd:section id=review round=2 -->
## Peer review

*Automated review. Reviewers and models: light `anthropic/claude-sonnet-5.5`, advanced:methodology `qwen/qwen3.8-27b`, advanced:statistics `qwen/qwen3.8-27b`, orchestrator `anthropic/claude-sonnet-5.5`. Registered analyses are never changed to satisfy a reviewer; robustness checks sit beside them.*

**Review outcome.** Round 2: 8 of 12 claims supported by the results after the authors' revision; 2 analytical issues open for a robustness round.

*Round 1: 14 issue(s); 10 of 12 claims supported by the results after the authors' revision; 3 analytical issues open for a robustness round.*

**Review synthesis after the responses.** The tables support a null pooled effect on accuracy (1.0 point, CI [-0.3, 2.4]) and three nominal arm-level H1 effects with p between 0.004 and 0.043. They do not support treating those effects as robust. With 44 uncorrected tests, the exclusion rerun (H1a) removes two of the three effects, and the Guide's interval barely clears zero. The most important caveat is that only Automated Flagging survives the low-knowledge exclusion, and then only at p=0.044. The E1 and E2 findings are unsupported because their tables are empty.

#### R1 · high · Answered with a robustness check · round 1

*E1.* The E1 table has empty est/se/p columns for every arm, yet the text claims that Automated Flagging (p=0.004) and AI Literacy Guide (p=0.043) became nonsignificant. Nothing displayed supports this. The 'attention-check failure' label is also misleading: pk_score<1 is a knowledge-question failure, not an attention check, and may be post-treatment-correlated or confounded with ability. Dropping 30% of the sample is not a clean robustness test.

**Response.** Added H1a, a robustness re-estimate of H1: exclude low political-knowledge respondents (pk_score<1), full estimates and CIs. H1: +0.010 (SE 0.007, p = 0.132, N = 2030). H1a: +0.009 (SE 0.006, p = 0.135, N = 1417).

#### R4 · medium · Answered with a robustness check · round 1

*H2.* The text says the other ten arms had estimates 'between −0.16 and 0.00', but the pooled random-effects result (−0.11, p=0.026) is reported as significant and tied to nothing in the narrative. The Breathing Exercise result (−0.54) has an SE of 0.23 that is much larger than the other arms' SEs, and arm-level SEs vary oddly (0.116 to 0.280), which suggests the Lin interaction model or outliers are driving them.

**Response.** Added H2a, a robustness re-estimate of H2: unadjusted difference in means, no covariates, same weights. H2: -0.111 (SE 0.050, p = 0.026, N = 2010). H2a: -0.134 (SE 0.054, p = 0.013, N = 2010).

#### R1 · high · Editorial · round 2

*E1 / E2.* The tables have empty estimate columns, yet the Finding lines claim effects were eliminated (E1) and that effects are not concentrated in either familiarity group and 'likely reflect sampling variability' (E2). The review flagged these claims as unsupported but the text still carries them. E1 is also still labelled 'attention-check failures', although pk_score<1 is a knowledge screen.

**Disposition.** The E1 and E2 tables are empty, so the conclusions must be deleted or the tables populated, and E1 needs relabelling as a low-knowledge exclusion.

#### R2 · high · Editorial · round 2

*H1 / H1a / Abstract.* H1a (dropping 613 low-knowledge respondents) shows Mindfulness becoming non-significant (p=0.12) and the Guide shrinking to 0.023 (p=0.39). Only Automated Flagging survives, at p=0.044. The H1a section has no prose, and the abstract and Key findings present all three H1 effects without this caveat. Excluding on pk_score could also be post-treatment if it was measured after treatment.

**Disposition.** The H1a estimates already exist, so the fix is prose that reports the non-robustness and when pk_score was measured.

#### R3 · high · Declined · round 2

*H1 / Key findings.* The three H1 effects are labelled 'Registered' and described as raising or lowering accuracy, but there are 44 uncorrected tests and p-values of 0.032 to 0.043. The Guide's CI lower bound is 0.2 points. The wording is too strong.

**Disposition.** The plan specifies no multiple-testing correction, so adjusted p-values would change the registered analysis. The wording can be softened to 'nominal' without it.

#### R4 · medium · Robustness check proposed · round 2

*H2.* The prose calls the pooled -0.11 a result and says 'one arm out of eleven could arise by chance'. The Breathing SE (0.23) is far larger than most other arms' SEs, which the review flagged. Pooled I² is 0 even though SEs vary widely. The unadjusted H2a Breathing estimate (-0.63) is also not discussed.

**Disposition.** Leverage and outlier diagnostics on the Lin model can be run on the same data, and H2a can be discussed in the text.

#### R5 · medium · Editorial · round 2

*Design.* IPW construction, exclusion rules and attrition by arm are not reported (227 respondents dropped). Control n=181 is much smaller than most treatment arms. Part of the data pre-dated registration, but it is not stated which arms or batches.

**Disposition.** The weights, exclusions, attrition by arm and pre-registration batches need documenting in the text.

#### R6 · medium · Editorial · round 2

*H5/H6 and Potential.* H6 interprets the pattern as a response-bias shift ('hints that some arms shift how people classify posts'), and the pooled H5 effect is reported as p=0.000. No discernment measure supports the bias reading. Breathing Exercise on real posts is -4.8 and not significant.

**Disposition.** The bias reading should be labelled speculative and the pooled p written as p<0.001.

#### R7 · low · Robustness check proposed · round 2

*E3.* The Finding line says 'max p = 0.816', which is garbled alongside 'all p > 0.116'. 'Confirming the randomisation' is also too strong for 11 null tests, and no joint test is given.

**Disposition.** A joint F-test of arm dummies on pk_score is a straightforward additional estimate, and the wording needs fixing too.

#### R8 · low · Editorial · round 2

*Related work.* The retrieved list includes irrelevant items (kidney disease, PRISMA-P, mortality risk), and the Capraro et al. characterisation is dubious (the paper concerns socioeconomic inequalities).

**Disposition.** The irrelevant references should be removed and the Capraro description corrected.

#### Claim checks

| Claim | Where | Verdict | Evidence | After revision |
|---|---|---|---|---|
| Pooled across arms, total accuracy was 1.0 point higher than control (95% CI [−0.3, 2.4]) | Abstract | **supported** | registered_summary H1:pooled: estimate 0.010, SE 0.007, p=0.132. The CI follows from the estimate and SE. | **supported**: Pooled across arms, total accuracy was 1.0 point higher than control (95% CI [−0.3, 2.4]) |
| Two arms raised accuracy: Automated Flagging by 4.4 points ... AI Literacy Guide by 4.7 points | Abstract | **overstated** | H1_arms: Automated Flagging 0.044, CI [0.014, 0.073], p=0.004. Guide 0.047, CI [0.002, 0.092], p=0.043. H1a: Guide 0.023, p=0.39. Automated Flagging 0.036, p=0.044. | **supported**: Automated Flagging nominally raised accuracy by 4.4 points ... AI Literacy Guide by 4.7 points |
| Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3]) | Abstract | **overstated** | H1_arms: -0.039, p=0.032. H1a: -0.037, CI [-0.083, 0.010], p=0.122. | **supported**: Mindfulness nominally lowered it by 3.9 points (95% CI [−7.4, −0.3]) |
| Registered: Automated Flagging raised total accuracy by 4.4 points (p=0.004) | Key findings | **overstated** | H1_arms row 3 matches the numbers. There are 44 uncorrected tests, and H1a gives p=0.044. | **supported**: Automated Flagging had 4.4 points higher total accuracy ... it also held when low-knowledge respondents were excluded (p=0.044) |
| Pooled across arms, attitudes toward AI were lower by 0.11 scale points (95% CI [−0.21, −0.01]) | Key findings | **supported** | H2 pooled: -0.111, SE 0.050, p=0.026. The unadjusted H2a pooled estimate is -0.134, p=0.013. | **supported**: Pooled across arms, attitudes toward AI were 0.11 scale points lower (95% CI [−0.21, −0.01]) |
| Attitudes toward AI were lower in the Breathing Exercise arm by 0.54 scale points (p=0.018) | H2 | **overstated** | H2 table: -0.543, CI [-0.994, -0.092], p=0.018. This is the only significant arm among 11. H2a gives -0.633, p=0.011. | **supported**: Attitudes toward AI were 0.54 scale points lower in the Breathing Exercise arm ... only one of eleven arms ... exploratory in character |
| Confidence fell in AI Literacy Infographic 2 by 0.69 and Flagging by 0.53; Inoculation raised it by 0.51 | H3 | **supported** | H3 table: -0.686 (p=0.0095), -0.525 (p=0.012), +0.509 (p=0.007). The text is hedged elsewhere. | **supported**: AI Literacy Infographic 2 by 0.69 and Flagging by 0.53 lower; Inoculation raised by 0.51 |
| Excluding 613 attention-check failures eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns) | E1 | **unsupported** | E1 table estimate columns are empty. H1a shows Automated Flagging still significant (p=0.044). The Guide p=0.39. The respondents are low-knowledge, not attention failures. | **overstated**: Excluding 613 attention-check failures eliminated the two nominally significant registered effects (Automated Flagging p=0.004→ns) |
| No arm reached p<0.05 in either subsample ... not concentrated ... likely reflect sampling variability | E2 | **unsupported** | E2 table has only n columns. The estimates and p-values are empty. | **unsupported**: No arm reached p<0.05 in either subsample ... likely reflect sampling variability |
| No intervention significantly affected pre-treatment knowledge (max p = 0.816), confirming the randomisation | E3 | **overstated** | E3: min p=0.116, max p=0.816. No joint test is given. | **overstated**: No intervention significantly affected pre-treatment knowledge (all p > 0.116, max p = 0.816), confirming the randomisation |
| Taken with H5, this hints that some arms shift how people classify posts rather than raising accuracy overall | H6 | **overstated** | H6: only Infographic 2 is significant (-0.061). H5 has three arms with higher detection. No discernment or bias measure exists. | **supported**: One might speculate that some arms shift how people classify posts, but ... it remains speculation |
| Pooling the 11 arm effects ... 0.038 (SE 0.011, p = 0.000) | H5 | **overstated** | The p-value is shown as 0.000. The pooled SE is approximate because the arms share a control group. | **overstated**: Pooling the 11 arm effects ... gives 0.038 (SE 0.011, p = 0.000) |

#### Editorial guidance and the authors' response

| # | Guidance | Response |
|---|---|---|
| G1 | Delete or populate the E1 and E2 findings, and relabel E1 as a low-knowledge exclusion. | E1 and E2 conclusions removed, E1 relabelled. |
| G2 | Add H1a prose to the abstract and Key findings: only Automated Flagging survives, at p=0.044, and the Mindfulness and Guide effects do not. | H1a added to the abstract and takeaways. |
| G3 | Describe the three H1 effects as nominal, since 44 tests were run uncorrected and the plan has no correction. | H1 effects described as nominal given 44 uncorrected tests. |
| G4 | State when pk_score was measured relative to treatment, and document the IPW weights, exclusions, attrition by arm and which batches pre-dated registration. | Design notes state what is undocumented (weights, exclusions, attrition, batches, pk_score timing); I could not supply details absent from the inputs. |
| G5 | Change E3 to 'min p=0.116, consistent with balance', and write the H5 pooled p as <0.001. | E3 wording changed; the pooled H5 p is not in the tables, so it was not added. |
| G6 | Remove the irrelevant references and correct the Capraro description. | The draft contained no literature references, so nothing was removed. |

#### Claims reworded in revision

- **K1.** Abstract now calls the accuracy effects nominal and uncorrected, and notes only Automated Flagging held under exclusion.
- **K2.** Mindfulness described as a nominal decrease, not robust to the exclusion.
- **K3.** Key finding now says nominal, uncorrected, and cites the H1a result (p=0.044).
- **K4.** H2 now reports H2a (−0.63, p=0.011) and calls the result isolated and exploratory in character.
- **K5.** E1 claim deleted and relabelled as a low-knowledge exclusion; points to H1a.
- **K6.** E2 conclusion deleted; the table has no estimates.
- **K7.** E3 now says min p=0.116, consistent with balance; no joint test is available in the tables, so none was added.
- **K8.** H6 bias reading presented as speculation.
- **K9.** The H5 pooled estimate is not in the supplied tables, so no pooled figure or p<0.001 was added; nothing changed.

#### Unresolved questions

- **U1.** Do the interventions change response bias (willingness to label posts as AI) rather than true discernment? Only share-correct scores exist, so there is no signal-detection measure to separate sensitivity from bias. Taken up by the proposed extensions *Signal-detection replication of labels and literacy guide* and *Discernment vs response bias: manipulating base rates*.
- **U2.** Do the Automated Flagging and AI Literacy Guide effects on accuracy replicate in a larger, independent sample with a pre-specified correction? The effects are marginal with 44 uncorrected tests and small arms, so this single study cannot distinguish them from chance. Taken up by the proposed extensions *Signal-detection replication of labels and literacy guide* and *Does label benefit depend on stimulus difficulty and AI familiarity?*.


<!-- fd:section id=potential -->
## Research potential

*An assessment by the pipeline of what this study can still become: what stands, why it may not have landed, the debates it bears on, and which follow-up is worth running. Written after the review; the proposed extensions below are built from it.*

**What stands.** Registered, multi-arm design with a shared control (n=181) and 11 interventions, so arms are directly comparable on one accuracy metric (control 69.3% correct). Lin-style covariate adjustment with HC2 SEs, and a random-effects pooled estimate (0.010, SE 0.007) that honestly shows the null overall. Decomposing accuracy into fake and real subscores (H5/H6) exposed a likely response-bias pattern: Breathing Exercise +9.1 points on AI posts, with authentic posts -4.8 (ns). Candid reporting of 44 uncorrected tests, so the nominal effects are flagged as fragile.

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Measurement | Only share-correct scores for fake and real posts were kept, so sensitivity (discernment) cannot be separated from a bias toward labelling posts as AI. | U1; H5 gains for Nudge, Breathing and Guide (+6.6, +9.1, +7.9) with no matching H6 gains. |
| Statistical power | Per-arm n of 78-333 against a control of 181 gives MDEs of 3.2-5.2 points on H1, so most arms could only detect effects as large as the headline ones. The two positive H1 effects sit near or below their MDEs, so they are likely inflated if real. | MDE Automated Flagging 0.042 vs observed 0.044; Guide 0.039 vs 0.047; Inoculation MDE 0.052; pooled effect 0.010. |
| Analysis | 44 registered tests with no multiplicity correction, and the exclusion, IPW and attrition documentation is missing. The nominal H1 effects (p=0.004, 0.043) cannot be told apart from noise. | Mindfulness -3.9 (p=0.032) and Guide +4.7 (p=0.043) are of similar strength; E1 and E2 tables are empty. |
| Design | Interventions differ in kind (labels on posts vs pre-feed training) and in dose, and the outcome is an immediate, single-session judgment. Each arm tests a bundle, so the mechanism is not isolated. | Arm descriptions; Automated Flagging adds a label to the posts, whereas the Guide acts only before the feed. |

**D1. Can individual-level interventions meaningfully improve resistance to misinformation?.** (a) Prebunking, inoculation and literacy tools shift belief and detection, so individual-level interventions are worthwhile. [Lewandowsky et al. (2021)] (b) Individual-level fixes are small and fragile, and system-level change is needed. [Chater et al. (2022), Ecker et al. (2022)] This study: Leans toward b: the pooled accuracy effect is 1 point (CI -0.3 to 2.4), and only labels from an automated detector showed a possibly real gain. The study cannot rule out small effects or speak to system-level reform.

**Verdict.** A follow-up is worthwhile but narrow. The pooled H1 effect is about 1 point and the two positive effects are nominal and near their MDEs, so the study mostly shows that these interventions are weak. The open question is whether anything improves discernment rather than bias, and the existing data cannot answer it. Run advance_design first: item-level signal detection, a registered multiplicity plan, and about 420 per arm. It settles U1 and U2 together. Run the base-rate design next only if d' shows a gain.


<!-- fd:section id=extensions -->
## Proposed extensions

*3 follow-up studies proposed by the pipeline from these results, each answering one of the reasons the study did not land (see Research potential). Survey designs ship as an importable Qualtrics file (`extensions/<id>.qsf`: in Qualtrics, Create project, Survey, How do you want to start: Import a QSF file); non-survey follow-ups are plans. Advanced: with a Qualtrics API token and the local Qualtrics MCP server, `filedrawer build-extension . <id>` creates the draft directly. They are proposals, not findings.*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Signal-detection replication of labels and literacy guide

The source study found Automated Flagging raised accuracy 4.4 points (CI 1.4 to 7.3) and the AI Literacy Guide 4.7 points (CI 0.2 to 9.2), but pooled accuracy was only 1 point (CI -0.3 to 2.4) across 44 uncorrected tests. Only share-correct scores were stored, so sensitivity and response bias could not be separated, and Breathing and Nudge arms raised AI detection without raising authentic recognition.

**Why this one.** Fixes the measurement failure: collects item-level real/AI judgments plus a confidence rating so d' and criterion can be estimated (U1), and gives a clean replication of the two nominal effects (U2).

**Debate it speaks to.** Can individual-level interventions meaningfully improve resistance to misinformation?: Prebunking, inoculation and literacy tools shift belief and detection, so individual-level interventions are worthwhile. versus Individual-level fixes are small and fragile, and system-level change is needed.

*Answers the open reviewer questions U1, U2 (see Peer review).*

**Hypothesis.** Automated labels and the literacy guide raise d' relative to control; if the effects are only criterion shifts, d' will not differ and c will move toward more AI responses.

**Design.** Control vs. Automated detector label vs. AI Literacy Guide; primary outcome: Sensitivity d' and criterion c from a multilevel signal-detection model (probit mixed model of AI judgment on true item status, arm, and their interaction, with random effects for respondent and item).

**Power.** About 420 per arm to detect 0.03 at 80% power (H1 observed 0.044 (Automated Flagging) shrunk toward the 0.03 MDE of the largest arm (0.0318 at n=333); a 3-point gain at 80% power needs roughly 420 per arm.).

Files: [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt) · [`extensions/advance_design.qsf`](extensions/advance_design.qsf) (1 media stimuli to supply after import)

#### Details: open items before fielding (advance_design)

- The 40 image files, their ground-truth labels and the detector label assets must be supplied by the research team.
- IRB approval number and participant compensation must be supplied.
- The treatment block for the control arm is intentionally empty; the label arm's flags are shown inside the item stimuli.
- Supply media: item1: image stimulus to supply (one of 40 photos, half AI-generated and half authentic, with a detector label sh)

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Does label benefit depend on stimulus difficulty and AI familiarity?

Automated Flagging raised accuracy by 4.4 points (p=0.004) in the source study, but the familiarity heterogeneity table (E2) was empty and some high-familiarity arm halves had n=38 or fewer. This follow-up tests whether the gain holds across easy vs hard stimuli and across prior AI familiarity, with enough power for an interaction test.

**Why this one.** Addresses the missing moderator: E2 was empty and underpowered, and the high-familiarity halves have n=38 or fewer in some arms.

*Answers the open reviewer question U2 (see Peer review).*

**Hypothesis.** H1: automated labels raise d' relative to control (0.035 minimum effect). H2: the label gain is smaller for hard (recent-generator) stimuli. H3: the label gain differs by ai_scale (high vs low familiarity).

**Design.** Control vs. Automated label; primary outcome: Discernment d' (z(hit rate) minus z(false-alarm rate)) across the 8 posts, with condition by difficulty and condition by ai_scale interaction tests.

**Power.** About 500 per arm to detect 0.035 at 80% power (H1 Automated Flagging 0.044, with a halved interaction detectable only with several hundred per cell.).

Files: [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt) · [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) (4 media stimuli to supply after import)

#### Details: open items before fielding (generalizability_conditional)

- The actual image and text stimuli, including older vs recent generator outputs, must be supplied by the research team.
- The automated label accuracy rate and wording must be fixed by the research team.
- Compensation and IRB approval number must be supplied by the research team.
- Supply media: ctrl_post1: image stimulus to supply (an AI-generated image from an older generator, shown as a social media post with)
- Supply media: ctrl_post2: image stimulus to supply (a screenshot of a social media text post written by a recent language model, wit)
- Supply media: lab_post1: image stimulus to supply (an AI-generated image from a recent generator, shown as a social media post with)
- Supply media: lab_post2: image stimulus to supply (a screenshot of an authentic social media text post with a banner reading 'Autom)

<!-- fd:ext id=theoretical_debate kind=alternative label=theoretical_debate -->
### Theoretical debate: Discernment vs response bias: manipulating base rates

The source found Breathing and Nudge raised detection of AI posts without raising recognition of authentic posts (H5 gains 0.066-0.091, SE about 0.03), which fits a bias toward answering AI. Pooled accuracy was only about 1 point (CI -0.3 to 2.4), so it is unclear whether individual interventions help. Changing the share of AI items separates a real sensitivity gain from a shifted answering criterion.

**Why this one.** Discriminates the two positions of D1 by separating bias from sensitivity. If interventions work, d' rises under any base rate. If the effects are bias, they vanish or flip when the share of AI items changes.

**Debate it speaks to.** Can individual-level interventions meaningfully improve resistance to misinformation?: Prebunking, inoculation and literacy tools shift belief and detection, so individual-level interventions are worthwhile. versus Individual-level fixes are small and fragile, and system-level change is needed.

*Answers the open reviewer question U1 (see Peer review).*

**Hypothesis.** If the interventions improve discernment, d' rises relative to control at both base rates and the intervention by base-rate interaction on d' is near zero. If they only bias responses toward answering AI, d' does not differ and c shifts toward AI responses, and this shift shrinks or reverses when 80% of items are AI.

**Design.** Control, 20% AI vs. Control, 80% AI vs. Breathing, 20% AI vs. Breathing, 80% AI vs. Guide, 20% AI vs. Guide, 80% AI; primary outcome: Signal-detection sensitivity d' per respondent, with criterion c as co-primary, computed from 20 item-level AI/authentic judgments.

**Power.** About 300 per arm to detect 0.04 at 80% power (H5 observed 0.066-0.091 with SE about 0.03; 300 per cell detects 0.04-0.05 at 80% power.).

Files: [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt) · [`extensions/theoretical_debate.qsf`](extensions/theoretical_debate.qsf) (14 media stimuli to supply after import)

#### Details: open items before fielding (theoretical_debate)

- The actual image and video files, the guide graphic and the item pools must be supplied by the research team.
- IRB approval number and compensation need to be set by the research team.
- The remaining 18 item/response pairs must be built from the same template.
- Supply media: item1: image stimulus to supply (feed item 1 from the 20% AI-share pool)
- Supply media: item2: image stimulus to supply (feed item 2 from the 20% AI-share pool)
- Supply media: item1: image stimulus to supply (feed item 1 from the 80% AI-share pool)
- Supply media: item2: image stimulus to supply (feed item 2 from the 80% AI-share pool)
- Supply media: item1: image stimulus to supply (feed item 1 from the 20% AI-share pool)
- Supply media: item2: image stimulus to supply (feed item 2 from the 20% AI-share pool)
- Supply media: item1: image stimulus to supply (feed item 1 from the 80% AI-share pool)
- Supply media: item2: image stimulus to supply (feed item 2 from the 80% AI-share pool)
- Supply media: guide_img: image stimulus to supply (annotated examples of AI artifacts in images and video frames)
- Supply media: item1: image stimulus to supply (feed item 1 from the 20% AI-share pool)
- Supply media: item2: image stimulus to supply (feed item 2 from the 20% AI-share pool)
- Supply media: guide_img: image stimulus to supply (annotated examples of AI artifacts in images and video frames)
- Supply media: item1: image stimulus to supply (feed item 1 from the 80% AI-share pool)
- Supply media: item2: image stimulus to supply (feed item 2 from the 80% AI-share pool)


<!-- fd:section id=appendix -->
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
| H1a | **robustness** | exclusions=[] | exclusions=["pk_score >= 1"] | responds to reviewer issue R1: exclude low political-knowledge respondents (pk_score<1), full estimates and CIs |
| H2a | **robustness** | estimator.kind="lin"; estimator.continuous=["media_trust", "pk_score", "ai_scale", "political_interest"]; estimator.categorical=null; estimator.covariates=["media_trust", "pk_score", "ai_scale", "political_interest"] | estimator.kind="diff_means"; estimator.continuous=[]; estimator.categorical=[]; estimator.covariates=[] | responds to reviewer issue R4: unadjusted difference in means, no covariates, same weights |

Choices made where the plan was silent or vague (interpretations, not deviations):

- H2 / outcome.reverse: "a six-item scale capturing whether AI is seen as an opportunity or threat" -> Items 4 and 6 (threat, manipulation) reverse-coded; higher = opportunity (The registration does not state the scoring direction)
- H4 / outcome.reverse: "a seven-item scale capturing willingness to believe and verify information" -> Items 3, 5, 6, 7 (distrust, verification) reverse-coded; higher = trust (The registration says '(dis)trust' without a scoring direction)
- H1 / estimator.robust: "Linear regression ... using the Lin (2013) estimator" -> HC2 robust standard errors, no clustering (The registration does not specify the variance estimator; one row per respondent)
- H1 / estimator.continuous: "media trust, political knowledge, AI usage, and political interest" -> All four covariates enter linearly (The registration lists the covariates without coding; the authors' script enters them linearly)

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
- `address_dryrun.log`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/advance_design.json`
- `extensions/advance_design.qsf`
- `extensions/advance_design.svg`
- `extensions/advance_design.txt`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
- `extensions/theoretical_debate.json`
- `extensions/theoretical_debate.qsf`
- `extensions/theoretical_debate.svg`
- `extensions/theoretical_debate.txt`
- `figures/E1_h1_no_attention_fail.png`
- `figures/E2_h1_ai_familiarity.png`
- `figures/H1_arms.png`
- `figures/H1a_arms.png`
- `figures/H2_arms.png`
- `figures/H2a_arms.png`
- `figures/H3_arms.png`
- `figures/H4_arms.png`
- `figures/H5_arms.png`
- `figures/H6_arms.png`
- `figures/badges/cost.svg`
- `figures/badges/data.svg`
- `figures/badges/design.svg`
- `figures/badges/provenance.svg`
- `figures/badges/registration.svg`
- `figures/badges/release.svg`
- `figures/badges/review.svg`
- `figures/design.svg`
- `figures/design.txt`
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
- `provenance/potential.json`
- `provenance/provenance.json`
- `provenance/review_before_address.json`
- `report.md`
- `responses.md`
- `results/E1_h1_no_attention_fail.csv`
- `results/E2_h1_ai_familiarity_heterogeneity.csv`
- `results/E3_placebo_pk_score.csv`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/H1a.csv`
- `results/H1a_arms.csv`
- `results/H2.csv`
- `results/H2_arms.csv`
- `results/H2a.csv`
- `results/H2a_arms.csv`
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
- `results.prev/H1.csv`
- `results.prev/H1_arms.csv`
- `results.prev/H1a.csv`
- `results.prev/H1a_arms.csv`
- `results.prev/H2.csv`
- `results.prev/H2_arms.csv`
- `results.prev/H2a.csv`
- `results.prev/H3.csv`
- `results.prev/H3_arms.csv`
- `results.prev/H4.csv`
- `results.prev/H4_arms.csv`
- `results.prev/H5.csv`
- `results.prev/H5_arms.csv`
- `results.prev/H6.csv`
- `results.prev/H6_arms.csv`
- `results.prev/analysis_tags.csv`
- `results.prev/registered_summary.csv`
- `review.json`
- `review.md`
- `run.log`
- `run.sh`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/04_exploratory.py`
- `study.json`
- `survey.qsf`
