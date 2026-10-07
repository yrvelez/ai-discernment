# Improving AI Discernment: do misinformation interventions help people spot AI-generated media?

*Yamil Velez · 2026-10-07 · N = 2,030 analysed of 2,257 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 12/12 claims supported](figures/badges/review.svg) [![plan: pre-registered #151,281](figures/badges/registration.svg)](https://aspredicted.org/q2eh95.pdf) ![status: draft](figures/badges/release.svg) [![DOI: 10.5281/zenodo.23166168](figures/badges/doi.svg)](https://doi.org/10.5281/zenodo.23166168) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $0.78](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-07; orchestrator `anthropic/claude-sonnet-5.5`, standard `qwen/qwen3.8-27b`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $0.78, 473k tokens in and 47k out. Cite as: Velez, Y. (2026). Improving AI Discernment: do misinformation interventions help people spot AI-generated media? [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://doi.org/10.5281/zenodo.23166168

<!-- fd:section id=abstract -->
## Abstract

Can misinformation interventions help people tell AI-generated media from authentic media? We ran a survey experiment on a US online panel (fielded October to November 2023) in which respondents were randomised to a control or one of 11 interventions before a feed-based discernment task. The analysis sample was 2,030 of 2,257 respondents. Four registered outcomes were total accuracy, attitudes toward AI, confidence in AI detection and trust in online information. Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3]), while Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3]). The AI Literacy Guide estimate (4.7 points, 95% CI [0.2, 9.2]) was borderline and uncorrected for multiple tests. Pooled across arms, accuracy was not distinguishable from control (+1.0 point, SE 0.7, p = 0.132). Some arms lowered attitudes toward AI or confidence in detection. Many tests were run without correction for multiple comparisons and several arms were small, so isolated effects should be read cautiously.

<!-- fd:section id=findings -->
## Key findings

- Most interventions did not measurably improve people's accuracy in spotting AI-generated media; pooled across 11 arms, accuracy was 1.0 point higher (SE 0.7, p = 0.132), not distinguishable from zero.
- Registered: Automated Flagging raised total accuracy by 4.4 points (95% CI [1.4, 7.3], p = 0.004). The AI Literacy Guide estimate (4.7 points) is borderline and uncorrected (95% CI [0.2, 9.2]).
- Registered: Mindfulness lowered total accuracy by 3.9 points (95% CI [−7.4, −0.3]). Two arms lowered confidence in AI detection, and one (Inoculation) raised it.
- Exploratory (post hoc): Breathing Exercise and the AI Accuracy Nudge raised detection of AI-generated posts, but these tests were not planned.
- Caveat: 44 registered arm-level tests were run with no multiplicity correction, and several arms are small (under 100), so isolated significant results may be chance.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 11 arms and a control group; online panel, United States. 2,257 responses were collected and 2,030 are analysed. The plan is pre-registered at https://aspredicted.org/q2eh95.pdf. Identifier and free-text columns removed before any model saw the data: none.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in United States (N = 2,030 analysed). Respondents are randomly assigned to 12 arms: Flagging, Provenance, Automated Flagging, AI Accuracy Nudge, Breathing Exercise, Mindfulness, Inoculation, AI Literacy Infographic, AI Literacy Infographic 2, AI Literacy Guide, AI Text Video, against the control group Control. Flagging: Posts in the feed are flagged as potentially AI-generated. Provenance: Posts carry information about the content's source and origin (provenance). Automated Flagging: Posts carry machine-learning-based AI-detection labels (automated flagging). AI Accuracy Nudge: Before the feed, an interactive task asks 'Is this image AI-generated?' (accuracy nudge). Breathing Exercise: Before the feed, a box-breathing exercise to reduce emotional reactivity. Mindfulness: Before the feed, a short mindfulness exercise. Inoculation: Before the feed, an inoculation message pre-exposing the respondent to manipulation techniques used in AI-generated media. AI Literacy Infographic: Before the feed, an infographic on how to identify AI-generated content. AI Literacy Infographic 2: Before the feed, an alternative infographic on how to identify AI-generated content. AI Literacy Guide: Before the feed, a comprehensive guide with examples of AI artifacts in images and videos. AI Text Video: Before the feed, an educational video about AI-generated text. Outcomes: Accuracy (share of 24 posts judged correctly), AI attitudes (opportunity vs threat, 6 items), Confidence in AI detection (single 7-point item), Trust in online information (7 items).


The study was registered on AsPredicted (#151,281) on 15 November 2023. Some data had already been collected at registration, but the later batches followed the plan. Of 2,257 raw respondents, 2,030 entered the analysis. Each arm was compared with the control group, and a few arms lost a handful of rows to missing values on attitude and trust items. Arms ranged from 78 to 333 respondents. Accuracy is a proportion correct. Tests are two-sided, and the p-values given are two-sided. The accuracy-split outcomes (detection of AI-generated posts and recognition of authentic posts) were not registered and are post hoc.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=registered outcome=total_score -->
### H1. Accuracy (share of 24 posts judged correctly)

*Each intervention changes AI-detection accuracy relative to control.*  
*Pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

Two interventions raised total accuracy relative to control. Automated Flagging was 4.4 points higher (95% CI [1.4, 7.3], p = 0.004), and the AI Literacy Guide 4.7 points higher (95% CI [0.2, 9.2], p = 0.043). Mindfulness was 3.9 points lower (95% CI [−7.4, −0.3], p = 0.032). The other eight arms had estimates between −1.0 and +2.0 points, with intervals that include zero. Pooled across arms the difference was +1.0 point (SE 0.7, p = 0.132). With 11 uncorrected comparisons, the Guide and Mindfulness results are near the threshold.

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

Attitudes toward AI were lower after the Breathing Exercise by 0.54 scale points (95% CI [−0.99, −0.09], p = 0.018). The other ten arms were not distinguishable from control, with intervals that include zero. Pooled across arms, attitudes were 0.11 points lower (SE 0.05, p = 0.026). The pooled shift is small, and the single-arm result is one of eleven uncorrected tests.

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

Confidence in detecting AI fell in two arms: AI Literacy Infographic 2 by 0.69 points (95% CI [−1.20, −0.17], p = 0.010) and Flagging by 0.53 points (95% CI [−0.94, −0.12], p = 0.012). Inoculation went the other way, raising confidence by 0.51 points (95% CI [0.14, 0.88], p = 0.007), though that arm is small (77 respondents). The other eight arms were not distinguishable from control. The pooled estimate was −0.13 (p = 0.177).

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

Trust in online information was lower after the AI Literacy Infographic by 0.15 points (95% CI [−0.27, −0.02], p = 0.023). The other ten arms were within about ±0.15 of control and not distinguishable from it. The pooled estimate was −0.04 (p = 0.060). With eleven uncorrected tests, the single-arm result is tentative.

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

![Planned treatment effects](figures/registered_effects.png)

<!-- fd:section id=exploratory-authors -->
## Exploratory analyses specified by the authors

*Not pre-registered. The authors specified these analyses after seeing the data; they are run by the same deterministic scripts as the registered tests and should be read as hypothesis-generating.*

<!-- fd:hyp id=H5 tag=exploratory outcome=fake_score -->
### H5. AI-content detection accuracy (share of 12 AI-generated posts identified)

*Not registered: each intervention changes detection of AI-generated posts relative to control.*  
*Exploratory, not pre-registered.*

![H5: effect by arm](figures/H5_arms.png)

This post hoc analysis looked at detection of AI-generated posts. Breathing Exercise raised it by 9.1 points (95% CI [3.2, 15.0], p = 0.003) and the AI Accuracy Nudge by 6.6 points (95% CI [1.4, 11.9], p = 0.014). The AI Literacy Guide was 7.9 points higher, with an interval barely excluding zero (95% CI [0.0, 15.7], p = 0.049). The other eight arms were not distinguishable from control.

Pooling the 11 arm effects with a random-effects model gives 0.038 (SE 0.011, p < 0.001; tau² 0.0002, I² 0.18). The arms share one control group, so this pooled standard error is approximate.

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

This post hoc analysis looked at recognition of authentic posts. AI Literacy Infographic 2 lowered it by 6.1 points (95% CI [−11.1, −1.0], p = 0.019). The other ten arms were not distinguishable from control, with intervals that include zero. Given the number of uncorrected tests, this single result is tentative.

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

_None produced._

<!-- fd:section id=related -->
## Related work

The retrieved list is thin and largely off-topic (genomics, microbiology, pharmacology), so direct prior findings on the study's hypotheses are scarce. The closest relevant evidence concerns whether individual-level behavioral interventions produce meaningful, generalizable effects. Chater and Loewenstein (2022) argue that an influential i-frame tradition—targeting individual cognition without modifying the surrounding system—has led behavioral public policy astray, which directly challenges the premise that interventions like those tested here (H1–H6) will yield robust shifts in detection accuracy, attitudes, confidence, or trust. Ruggeri et al. (2023) assessed 747 pandemic-related behavioral-science articles and found the evidence base to be thin and often inconsistent, further tempering expectations for small-scale intervention effects. No retrieved work directly addresses AI-detection accuracy or attitudes toward AI-generated content.

The live disagreement is between the i-frame assumption embedded in the study's design and the s-frame critique of Chater and Loewenstein (2022): the study tests whether individual-level levers shift measurable outcomes, while that critique holds such levers are insufficient without system-level change. Ruggeri et al. (2023) add a second layer of skepticism by showing that even when individual-level interventions are tested, effects are frequently underpowered or inconsistent. The study's controlled design with multiple outcomes can speak to whether the specific interventions produce detectable individual-level effects, but it cannot resolve the broader s-frame question of whether those effects translate into system-level outcomes. Methodologically, Keogh-Brown et al. (2007) flag contamination as a persistent threat in educational-intervention trials, relevant here if interventions involve shareable information.

Retrieved works (OpenAlex; queries: inoculation AI-generated media detection accuracy experimental; accuracy nudge misinformation detection confidence trust survey; inoculation backfire overconfidence misinformation intervention null effect; misinformation intervention transfer generalization failure deepfake detection; experimental survey multiple treatment arms Lin estimator covariate adjustment detection accuracy):

- Nick Schurch, Pietá Schofield, Marek Gierliński, Christian Cole (2016). How many biological replicates are needed in an RNA-seq experiment and which differential expression tool should you use?. RNA. https://doi.org/10.1261/rna.053959.115
- Joana Azeredo, Nuno F. Azevedo, Romain Briandet, Nuno Cerca (2016). Critical review on biofilm methods. Critical Reviews in Microbiology. https://doi.org/10.1080/1040841x.2016.1208146
- Jean‐Christophe Lagier, S. Khelaifia, Maryam Tidjani Alou, Sokhna Ndongo (2016). RETRACTED ARTICLE: Culture of previously uncultured members of the human gut microbiota by culturomics. Nature Microbiology. https://doi.org/10.1038/nmicrobiol.2016.203
- Nick Chater, George F. Loewenstein (2022). The i-frame and the s-frame: How focusing on individual-level solutions has led behavioral public policy astray. Behavioral and Brain Sciences. https://doi.org/10.1017/s0140525x22002023
- Nick Chater, George F. Loewenstein (2022). The i-Frame and the s-Frame: How Focusing on Individual-Level Solutions Has Led Behavioral Public Policy Astray. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.4046264
- Kai Ruggeri, Friederike Stock, S. Alexander Haslam, Valerio Capraro (2023). A synthesis of evidence for policy from behavioural science during COVID-19. Nature. https://doi.org/10.1038/s41586-023-06840-9
- Lara Marques, Bárbara Costa, Mariana Pereira, Abigail Silva (2024). Advancing Precision Medicine: A Review of Innovative In Silico Approaches for Drug Development, Clinical Pharmacology and Personalized Healthcare. Pharmaceutics. https://doi.org/10.3390/pharmaceutics16030332
- Ruocheng Guo, Lu Cheng, Jundong Li, P. Richard Hahn (2020). A Survey of Learning Causality with Data. ACM Computing Surveys. https://doi.org/10.1145/3397269
- Marcus Richard Keogh-Brown, Max Oscar Bachmann, Lee Shepstone, Catherine Elizabeth Hewitt (2007). Contamination in trials of educational interventions. Health Technology Assessment. https://doi.org/10.3310/hta11430
- Yehudit Hasin-Brumshtein, Marcus Michael Seldin, Aldons Jake Lusis (2017). Multi-omics approaches to disease. Genome biology. https://doi.org/10.1186/s13059-017-1215-1

<!-- fd:section id=limitations -->
## Limitations

The study ran 44 arm-level tests on registered outcomes and 22 more post hoc, with no correction for multiple comparisons, so some of the significant results are probably chance. Several arms are small, notably Inoculation (78) and the two AI Literacy Infographics (about 80–100), which limits precision. Some data were collected before registration, though later batches followed the plan. The panel is a US online sample, so the results may not generalise. Outcomes were measured right after the intervention, so durability is unknown. Detection of AI-generated posts and recognition of authentic posts were not registered, and the Breathing Exercise and Flagging patterns across outcomes are hard to interpret.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Registered analyses are never changed.*

**Outcome.** 12 of 12 checked claims supported after the agent's corrections; 4 of 4 registered analyses run as planned; 3 reworded; 1 text fix; 2 correction passes.

#### Corrections

- **Corrected** · 4 items reworded or fixed in the text: Abstract, Key findings, H5, R1, Abstract / H1 / Key findings. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The arm-level estimates in the text match the tables. Automated Flagging (+4.4), the AI Literacy Guide (+4.7) and Mindfulness (−3.9) are significant on accuracy at uncorrected p-values, and the pooled accuracy effect is null. The main caveat is that 44 registered tests were run with no correction, so the Guide (p = 0.043) and Mindfulness (p = 0.032) results are fragile. Some wording overreaches, notably that exploratory and uncorrected findings are described as raising or lowering outcomes, and the Key findings sentence on Breathing Exercise and the Accuracy Nudge omits the Guide. The pooled CIs are not tabulated but follow from the pooled estimate and SE.

| Registered analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |
| H2 | as planned | — | — |
| H3 | as planned | — | — |
| H4 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K1 | medium | presentational | claims | Fixed in text | Abstract: Overstated claim: "AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2])". H1 table: 0.047, CI [0.002, 0.092], p = 0.043; the interval barely excludes zero and is uncorrected across 11 arms *claim checked against the tables by the checking agent* |
| K2 | medium | presentational | claims | Fixed in text | Key findings: Overstated claim: "Several arms also lowered confidence in AI detection". H3: only Flagging and Infographic 2 are significantly negative; Inoculation is significantly positive *claim checked against the tables by the checking agent* |
| K3 | medium | presentational | claims | Fixed in text | H5: Overstated claim: "AI Literacy Guide 7.9 points higher, CI [0.04, 15.7]". H5 table: CI [0.000, 0.157], p = 0.0488 *claim checked against the tables by the checking agent* |
| R1 | medium | presentational | light | Fixed in text | Abstract / H1 / Key findings: The text gives a pooled accuracy difference of +1.0 point with 95% CI [−0.3, +2.4]. The table shows only pooled estimate 0.010, SE 0.007 and p 0.132. No CI appears in any table. The implied CI is about [−0.003, 0.023], so the stated bounds roughly match but are not tabulated. *The pooled CI is derivable from the estimate and SE, so only reporting needs fixing.* |
| R2 | low | presentational | light | Fixed in text | H5: The text gives the AI Literacy Guide CI as [0.04, 15.7]. The table shows [0.000, 0.157], so the lower bound is about 0.0 points, not 0.04. The p-value is 0.0488, consistent with a lower bound very near zero. *The H5 Guide CI lower bound should read 0.0 as in the table.* |
| R3 | low | presentational | light | Fixed in text | H2: The text gives the pooled AI attitudes estimate as −0.11 (95% CI [−0.21, −0.01]). The table has only −0.111 (SE 0.050, p = 0.026), and no CI is tabulated. *Report the pooled SE and p, or add the CI to the table.* |
| R4 | low | presentational | light | Fixed in text | H3 / H4: The pooled CIs in the text (H3: [−0.32, +0.06]; H4: [−0.08, +0.00]) do not appear in any table. Only the pooled estimates, SEs and p-values do. *The pooled CIs for H3 and H4 need tabulating or replacing with SE and p.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3]) | Abstract | supported | H1 table: 0.044, CI [0.014, 0.073], p = 0.0035 | supported: Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3]) |
| AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2]) | Abstract | overstated | H1 table: 0.047, CI [0.002, 0.092], p = 0.043; the interval barely excludes zero and is uncorrected across 11 arms | supported: The AI Literacy Guide estimate (4.7 points, 95% CI [0.2, 9.2]) was borderline and uncorrected for multiple tests |
| Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3]) | Abstract | supported | H1 table: −0.039, CI [−0.074, −0.003], p = 0.032 | supported: Mindfulness lowered it by 3.9 points (95% CI [−7.4, −0.3]) |
| Pooled across arms, accuracy was not distinguishable from control (+1.0 point, 95% CI [−0.3, +2.4]) | Abstract | supported | H1 pooled: 0.010, SE 0.007, p = 0.132; the implied CI is about [−0.003, 0.024] | supported: Pooled across arms, accuracy was not distinguishable from control (+1.0 point, SE 0.7, p = 0.132) |
| Some arms lowered attitudes toward AI or confidence in detection | Abstract | supported | H2 Breathing Exercise −0.543, p = 0.018; H3 Flagging −0.525 and Infographic 2 −0.686 | supported: Some arms lowered attitudes toward AI or confidence in detection |
| Most interventions did not measurably improve accuracy | Key findings | supported | H1: 8 of 11 arms have CIs including zero | supported: Most interventions did not measurably improve people's accuracy; pooled 1.0 point higher (SE 0.7, p = 0.132) |
| Breathing Exercise and the AI Accuracy Nudge raised detection of AI-generated posts | Key findings | supported | H5: Breathing Exercise 0.091, p = 0.0027; Nudge 0.066, p = 0.0135; labelled exploratory | supported: Breathing Exercise and the AI Accuracy Nudge raised detection of AI-generated posts, but these tests were not planned |
| Several arms also lowered confidence in AI detection | Key findings | overstated | H3: only Flagging and Infographic 2 are significantly negative; Inoculation is significantly positive | supported: Two arms lowered confidence in AI detection, and one (Inoculation) raised it |
| Attitudes pooled 0.11 points lower (95% CI [−0.21, −0.01], p = 0.026) | H2 | supported | H2 pooled −0.111, SE 0.050, p = 0.026 | supported: Pooled across arms, attitudes were 0.11 points lower (SE 0.05, p = 0.026) |
| AI Literacy Guide 7.9 points higher, CI [0.04, 15.7] | H5 | overstated | H5 table: CI [0.000, 0.157], p = 0.0488 | supported: The AI Literacy Guide was 7.9 points higher, with an interval barely excluding zero (95% CI [0.0, 15.7], p = 0.049) |
| 44 arm-level tests ... no multiplicity correction | Key findings | supported | 4 outcomes × 11 arms = 44; the plan specifies no correction | supported: 44 registered arm-level tests were run with no multiplicity correction |

Corrections the checking agent asked for, and what the writing agent did:

- G1. Tabulate the pooled CIs or report pooled SEs instead. Done: Pooled CIs removed from the text; pooled estimates are given with SE or p-value instead.

Re-check of the corrected text: No further rewording is needed; all previously flagged issues are resolved and the new claims match the tables.

#### Other review options

- **Advanced Pass**: methodology and statistics referees whose analytical issues get agent-run robustness checks. `--review light,advanced`
- **Coarse**: the open-source coarse-ink reviewer, run locally (about $1-2). `--review light,coarse`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview**: import any referee report, e.g. one posted on an OpenReview submission. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Randomised 11 interventions against a shared control with a registered plan (AsPredicted #151,281), using Lin covariate adjustment and HC2 SEs. This gives a clean, comparable arm-by-arm estimate on four outcomes. Reported every arm for every outcome with CIs, and said plainly that the 44 registered tests were uncorrected and the pooled effect on accuracy was null (+1.0 point, SE 0.7, p = 0.132). Split accuracy into AI-post detection and authentic-post recognition, and flagged the split as post hoc. This exposes a possible response-bias pattern: Breathing Exercise +9.1 points on detection with authentic recognition −4.8, and Infographic 2 −6.1 on authentic. Included self-reported confidence and trust alongside accuracy, so the study can show calibration or backfire effects such as Inoculation raising confidence by 0.51 with no accuracy gain.

**Verdict.** A follow-up is worth running, but narrowly: only Automated Flagging (+4.4, p=0.004) looks like a real accuracy gain, and the pooled null (+1.0) and uncorrected tests warn against reading the rest. Run advance_design first. It replicates the label effect at adequate power and splits discernment from bias, which the current total accuracy score cannot do. The literature retrieved is mostly off-topic, so the only live debate is the i-frame versus s-frame framing, and the second brief tests it only indirectly.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Statistical power | Per-arm MDEs on accuracy are 3.2 to 5.2 points, about as large as the only significant effects. The significant arms are therefore likely overestimates, and the small arms cannot rule out realistic effects. | Power table H1: MDE 0.0318 (Nudge) to 0.0517 (Inoculation, n=78); Automated Flagging 0.044 vs MDE 0.042; Guide 0.047 vs MDE 0.039. |
| Analysis | Three of 11 accuracy arms cross p<0.05 with no multiplicity correction. Guide (p=0.043) and Mindfulness (p=0.032) would not survive any correction, and only Automated Flagging (p=0.004) is arguably robust. The pooled null contradicts a broad effect. | H1 table; pooled +0.010, p=0.132; 44 registered tests uncorrected. |
| Measurement | Total accuracy mixes detecting AI posts with accepting real ones, so a shift in scepticism looks like discernment gain or loss. Discernment (sensitivity) and bias were never separated, and the split outcomes were unregistered. | H5 Breathing +0.091 on AI posts but H6 −0.048 on real posts, with H1 only +0.015. |
| Design | Arms vary in content, dose and timing (labels in the feed vs pre-feed exercises), and the design cannot say which component works. Arm sizes are unbalanced (78 to 333) against a control of 181, and some data were collected before registration. | Arms ranged 78–333 against n=181 control; registration note on batches 1–2. |
| Framing | The literature retrieved is almost entirely off-topic, so the study is not positioned against prior work on inoculation, accuracy nudges or AI-detection literacy. The only live framing, i-frame versus s-frame, is not something the design tests. | Related work: only Chater & Loewenstein and Ruggeri et al. are relevant; no AI-detection papers retrieved. |

**D1. Individual-level (i-frame) fixes vs system-level (s-frame) change.** (a) Cheap individual-level interventions such as labels, nudges and literacy content can measurably improve people's handling of AI-generated media. (b) Individual-level levers yield small, inconsistent effects, and meaningful change needs system-level measures such as platform-level or provenance infrastructure. [Chater et al. (2022), Chater et al. (2022), Ruggeri et al. (2023)] This study: Leans to b for educational and mindfulness-type interventions: pooled accuracy +1.0 point (p=0.132), with several arms null or harmful. Automated Flagging (+4.4), a system-supplied label, is the clearest gain, which weakly fits the s-frame view. The study cannot test system-level effects.


<!-- fd:section id=extensions -->
## Proposed extensions

*3 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Separating discernment from response bias in machine-label interventions

Fixes measurement and power. It registers signal-detection outcomes (d′ and criterion) and replicates the one robust arm with an adequate sample.

**Hypothesis.** H1: Automated Flagging raises d-prime relative to control (not only a criterion shift). H2: 80%-accurate labels yield a smaller d-prime gain than 100%-accurate labels. H3: The Guide raises d-prime less than Automated Flagging.

**Design.** Control vs. Automated Flagging 100% vs. Automated Flagging 80% vs. AI Literacy Guide; primary outcome: d-prime (sensitivity) from 40 judgments, with criterion and total accuracy as co-registered outcomes. About 230 per arm for 80% power.

Files: [`extensions/advance_design.qsf`](extensions/advance_design.qsf) · [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt)

#### Details: background and open items (advance_design)

Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3], p=0.004), but accuracy cannot show whether labels improved sensitivity or merely shifted willingness to say AI; detection and real-content accuracy were not registered. With 44 uncorrected tests and small arms, the effect also needs replication with adequate power.

**Debate it speaks to.** Individual-level (i-frame) fixes vs system-level (s-frame) change: Cheap individual-level interventions such as labels, nudges and literacy content can measurably improve people's handling of AI-generated media. versus Individual-level levers yield small, inconsistent effects, and meaningful change needs system-level measures such as platform-level or provenance infrastructure.

**Power.** About 230 per arm to detect 0.03 at 80% power (H1 Automated Flagging estimate 0.044, observed SD ~0.13; 80% power for ~0.04 needs ~165 per arm, inflated for Holm correction and the weaker label-accuracy arms).

Open items before fielding:

- The 40 real and AI-generated post media files and the label assignment for the 80% arm must be supplied by the research team.
- IRB approval number and compensation amount.
- Supply media: judge_posts: set the matrix recode values after import AI-generated=1, Not AI-generated=0

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Does the label effect hold for newer generators and low-trust respondents?

Fixes sample and stimulus limits: the 2023 stimuli and US panel may not generalise, and the pooled null may hide moderation.

**Hypothesis.** H1: Automated Flagging raises accuracy and d-prime relative to control. H2: The gain is smaller for current-generation stimuli. H3: The gain differs between low and high baseline media trust (median split, pre-registered).

**Design.** Control vs. Automated Flagging; primary outcome: Accuracy (share of posts judged correctly) and d-prime. About 350 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items (generalizability_conditional)

Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3], p = 0.004) but the pooled effect across 11 arms was only +1.0 (SE 0.7), and stimuli were 2023-era with a US panel. Realism of current generators and baseline media trust may moderate the label effect, and durability was never measured.

**Power.** About 350 per arm to detect 0.04 at 80% power (Interaction effects need roughly 4x the n of the main effect 0.044; MDE for the 0.0318–0.042 range in H1).

Open items before fielding:

- Current-generation synthetic images and video and matched authentic posts must be produced by the research team.
- Compensation, IRB number and the re-contact wave instrument are to be supplied by the research team.
- Exact label accuracy for Automated Flagging must match the source study.
- Supply media: post_set: image stimulus to supply (2023-era synthetic or authentic post from the older-generator set)
- Supply media: post_set: image stimulus to supply (current-generation synthetic or authentic post from the newer-generator set)
- Supply media: post_label_auto: image stimulus to supply (machine-learning AI-detection label displayed under the post with a detection sc)

<!-- fd:ext id=theoretical_debate kind=alternative label=theoretical_debate -->
### Theoretical debate: Individual literacy vs system-supplied cue: which carries the effect?

Fixes design confounding: it separates cue content from attention or priming effects, which the original arms bundled.

**Hypothesis.** H1 (s-frame): real labels raise accuracy and d-prime, while the Guide alone and the placebo label do not. H2 (i-frame): the Guide alone or the placebo label raises accuracy and d-prime comparably to real labels. H3: the label x Guide interaction is positive if training makes labels more useful.

**Design.** Control vs. Real label vs. Guide only vs. Label plus Guide vs. Placebo label; primary outcome: Accuracy: share of 40 posts judged correctly, with d-prime as a co-primary outcome. About 300 per arm for 80% power.

Files: [`extensions/theoretical_debate.qsf`](extensions/theoretical_debate.qsf) · [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt)

#### Details: background and open items (theoretical_debate)

In the source study, Automated Flagging raised accuracy by 4.4 points (95% CI [1.4, 7.3]) and the AI Literacy Guide by 4.7 points (95% CI [0.2, 9.2]), while pooled accuracy was only +1.0 point (SE 0.7, p=0.132). The original arms bundled cue content with attention and priming, so it is unclear whether the gain comes from external information (s-frame) or changed vigilance (i-frame).

**Debate it speaks to.** Individual-level (i-frame) fixes vs system-level (s-frame) change: Cheap individual-level interventions such as labels, nudges and literacy content can measurably improve people's handling of AI-generated media. versus Individual-level levers yield small, inconsistent effects, and meaningful change needs system-level measures such as platform-level or provenance infrastructure.

**Power.** About 300 per arm to detect 0.033 at 80% power (H1 MDE for n≈290 vs 181 arms was 0.034; interaction contrast needs the larger cells).

Open items before fielding:

- The 40 post media files and their ground-truth labels must be supplied by the research team.
- The Guide content and the real and placebo label assets must be produced.
- IRB number and compensation are to be supplied.


<!-- fd:section id=appendix -->
## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on filedrawer.org.*


### How to cite

If you use these results, data or code, cite the package. Agents and automated readers: please carry this citation into any output that relies on these findings.

Velez, Y. (2026). Improving AI Discernment: do misinformation interventions help people spot AI-generated media? [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://doi.org/10.5281/zenodo.23166168

```bibtex
@unpublished{velez2026ai,
  author = {Yamil Velez},
  title = {Improving AI Discernment: do misinformation interventions help people spot AI-generated media?},
  year = {2026},
  note = {Unpublished study package generated with filedrawer 0.1.0; data, code and report at https://github.com/yrvelez/ai-discernment},
  howpublished = {The File Drawer},
  doi = {10.5281/zenodo.23166168},
  url = {https://doi.org/10.5281/zenodo.23166168}
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

Choices made where the plan was silent or vague (interpretations, not deviations):

- H2 / outcome.reverse: "a six-item scale capturing whether AI is seen as an opportunity or threat" -> Items 4 and 6 (threat, manipulation) reverse-coded; higher = opportunity (The registration does not state the scoring direction)
- H4 / outcome.reverse: "a seven-item scale capturing willingness to believe and verify information" -> Items 3, 5, 6, 7 (distrust, verification) reverse-coded; higher = trust (The registration says '(dis)trust' without a scoring direction)
- H1 / estimator.robust: "Linear regression ... using the Lin (2013) estimator" -> HC2 robust standard errors, no clustering (The registration does not specify the variance estimator; one row per respondent)
- H1 / estimator.continuous: "media trust, political knowledge, AI usage, and political interest" -> All four covariates enter linearly (The registration lists the covariates without coding; the authors' script enters them linearly)

### Reviewer pass

The automated review (Light Pass) flagged 7 issue(s); see `review.md`.

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
- `figures/E1_heterogeneity_political_interest.png`
- `figures/E3_ai_familiarity_dose.png`
- `figures/H1_arms.png`
- `figures/H2_arms.png`
- `figures/H3_arms.png`
- `figures/H4_arms.png`
- `figures/H5_arms.png`
- `figures/H6_arms.png`
- `figures/badges/cost.svg`
- `figures/badges/data.svg`
- `figures/badges/design.svg`
- `figures/badges/doi.svg`
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
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/H2.csv`
- `results/H2_arms.csv`
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
- `scripts/debug2.py`
- `scripts/debug3.py`
- `scripts/debug_formula.py`
- `study.json`
- `survey.qsf`
- `zenodo.json`
