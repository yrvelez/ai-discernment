# =============================================================================
# Replication Script: Improving AI Discernment
# =============================================================================
# Columbia University | IRB Protocol: AAAU9484
# =============================================================================

library(tidyverse)
library(estimatr)  # for lm_lin with Lin (2013) covariate adjustment
library(broom)     # for tidy()
library(metafor)   # for random effects meta-analysis

# =============================================================================
# 1. LOAD DATA
# =============================================================================

dat <- read_csv("data/replication_data.csv")

cat("Data loaded:", nrow(dat), "rows,", ncol(dat), "columns\n\n")

# Treatment labels
treatment_labels <- c(
  "0" = "Control",
  "1" = "Flagging",
  "2" = "Provenance",
  "3" = "Automated Flagging",
  "4" = "AI Accuracy Nudge",
  "5" = "Breathing Exercise",
  "6" = "Mindfulness",
  "7" = "Inoculation",
  "8" = "AI Literacy Infographic",
  "9" = "AI Literacy Infographic 2",
  "10" = "AI Literacy Guide",
  "11" = "AI Text Video"
)

# =============================================================================
# 2. PREPARE DATA
# =============================================================================

# Create ai_scale from subscription variables
analysis_data <- dat %>%
  filter(!is.na(treatment)) %>%
  filter(!is.na(total_score)) %>%
  mutate(
    # ai_scale: proportion of AI tools used (7 tools)
    ai_scale = (chatgpt + bing + claude + character + dalle + midjourney + stable_diff) / 7,
    # Treatment as factor with Control as reference
    treatment = factor(treatment, levels = 0:11, labels = names(treatment_labels))
  )

cat("Analysis sample:", nrow(analysis_data), "\n\n")

# Treatment distribution
cat("Treatment distribution:\n")
print(table(analysis_data$treatment))
cat("\n")

# =============================================================================
# 3. ESTIMATE TREATMENT EFFECTS - TOTAL ACCURACY (DISCERNMENT)
# =============================================================================

cat(strrep("=", 70), "\n")
cat("TOTAL ACCURACY (DISCERNMENT) RESULTS\n")
cat("Model: lm_lin with Lin (2013) covariate adjustment\n")
cat("Weights: 1/pr (inverse probability weights)\n")
cat("SEs: Cluster-robust (clustered by participant_id)\n")
cat(strrep("=", 70), "\n\n")

# Lin (2013) covariate adjustment:
# outcome ~ treatment, ~ covariates
# Includes treatment * (covariate - mean(covariate)) interactions

lm_total <- lm_lin(
  total_score ~ treatment,
  covariates = ~ media_trust + political_interest + pk_score + ai_scale,
  data = analysis_data,
  weights = 1/pr,
  clusters = participant_id
)

cat("Complete cases:", nobs(lm_total), "\n\n")

# Print treatment effects
cat("Treatment Effects on Total Accuracy:\n\n")
summary(lm_total)

# Extract just treatment coefficients (main effects only, not interactions)
coef_total <- tidy(lm_total) %>%
  filter(grepl("^treatment[0-9]+$", term)) %>%
  mutate(
    treatment = gsub("treatment", "", term),
    ci_lower = estimate - 1.96 * std.error,
    ci_upper = estimate + 1.96 * std.error
  ) %>%
  arrange(desc(estimate))

cat("\n\nTreatment Effects Summary (sorted by effect):\n")
coef_total %>%
  select(treatment, estimate, std.error, ci_lower, ci_upper, p.value) %>%
  mutate(across(c(estimate, std.error, ci_lower, ci_upper), ~round(., 4)),
         p.value = round(p.value, 4)) %>%
  as.data.frame() %>%
  print(row.names = FALSE)

# =============================================================================
# 4. ESTIMATE TREATMENT EFFECTS - AI DETECTION (FAKE CONTENT)
# =============================================================================

cat("\n\n", strrep("=", 70), "\n")
cat("AI DETECTION ACCURACY (FAKE CONTENT) RESULTS\n")
cat(strrep("=", 70), "\n\n")

lm_fake <- lm_lin(
  fake_score ~ treatment,
  covariates = ~ media_trust + political_interest + pk_score + ai_scale,
  data = analysis_data,
  weights = 1/pr,
  clusters = participant_id
)

cat("Complete cases:", nobs(lm_fake), "\n\n")

coef_fake <- tidy(lm_fake) %>%
  filter(grepl("^treatment[0-9]+$", term)) %>%
  mutate(
    treatment = gsub("treatment", "", term),
    ci_lower = estimate - 1.96 * std.error,
    ci_upper = estimate + 1.96 * std.error
  ) %>%
  arrange(desc(estimate))

cat("Treatment Effects on AI Detection:\n")
coef_fake %>%
  select(treatment, estimate, std.error, ci_lower, ci_upper, p.value) %>%
  mutate(across(c(estimate, std.error, ci_lower, ci_upper), ~round(., 4)),
         p.value = round(p.value, 4)) %>%
  as.data.frame() %>%
  print(row.names = FALSE)

# =============================================================================
# 5. ESTIMATE TREATMENT EFFECTS - NON-AI ACCURACY (REAL CONTENT)
# =============================================================================

cat("\n\n", strrep("=", 70), "\n")
cat("NON-AI ACCURACY (REAL CONTENT) RESULTS\n")
cat(strrep("=", 70), "\n\n")

lm_real <- lm_lin(
  real_score ~ treatment,
  covariates = ~ media_trust + political_interest + pk_score + ai_scale,
  data = analysis_data,
  weights = 1/pr,
  clusters = participant_id
)

cat("Complete cases:", nobs(lm_real), "\n\n")

coef_real <- tidy(lm_real) %>%
  filter(grepl("^treatment[0-9]+$", term)) %>%
  mutate(
    treatment = gsub("treatment", "", term),
    ci_lower = estimate - 1.96 * std.error,
    ci_upper = estimate + 1.96 * std.error
  ) %>%
  arrange(desc(estimate))

cat("Treatment Effects on Non-AI Accuracy:\n")
coef_real %>%
  select(treatment, estimate, std.error, ci_lower, ci_upper, p.value) %>%
  mutate(across(c(estimate, std.error, ci_lower, ci_upper), ~round(., 4)),
         p.value = round(p.value, 4)) %>%
  as.data.frame() %>%
  print(row.names = FALSE)

# =============================================================================
# 6. SUMMARY
# =============================================================================

cat("\n\n", strrep("=", 70), "\n")
cat("SUMMARY\n")
cat(strrep("=", 70), "\n\n")

cat("Total N:", nrow(analysis_data), "\n")
cat("Number of treatments:", n_distinct(analysis_data$treatment), "\n")

# Significant effects
sig_total <- coef_total %>% filter(p.value < 0.05)
sig_fake <- coef_fake %>% filter(p.value < 0.05)
sig_real <- coef_real %>% filter(p.value < 0.05)

cat("\nSignificant effects (p < 0.05):\n")
cat("  Total Accuracy:", nrow(sig_total), "\n")
if (nrow(sig_total) > 0) {
  for (i in 1:nrow(sig_total)) {
    cat(sprintf("    - %s: %.4f (p = %.4f)\n",
                sig_total$treatment[i], sig_total$estimate[i], sig_total$p.value[i]))
  }
}

cat("  AI Detection:", nrow(sig_fake), "\n")
if (nrow(sig_fake) > 0) {
  for (i in 1:nrow(sig_fake)) {
    cat(sprintf("    - %s: %.4f (p = %.4f)\n",
                sig_fake$treatment[i], sig_fake$estimate[i], sig_fake$p.value[i]))
  }
}

cat("  Non-AI Accuracy:", nrow(sig_real), "\n")
if (nrow(sig_real) > 0) {
  for (i in 1:nrow(sig_real)) {
    cat(sprintf("    - %s: %.4f (p = %.4f)\n",
                sig_real$treatment[i], sig_real$estimate[i], sig_real$p.value[i]))
  }
}

# Marginal effects
marginal_total <- coef_total %>% filter(p.value >= 0.05 & p.value < 0.10)
cat("\nMarginally significant effects (0.05 <= p < 0.10):\n")
cat("  Total Accuracy:", nrow(marginal_total), "\n")
if (nrow(marginal_total) > 0) {
  for (i in 1:nrow(marginal_total)) {
    cat(sprintf("    - %s: %.4f (p = %.4f)\n",
                marginal_total$treatment[i], marginal_total$estimate[i], marginal_total$p.value[i]))
  }
}

# =============================================================================
# 7. RANDOM EFFECTS META-ANALYSIS
# =============================================================================

cat("\n\n", strrep("=", 70), "\n")
cat("RANDOM EFFECTS META-ANALYSIS\n")
cat("Pooling treatment effects across all 11 interventions (REML)\n")
cat(strrep("=", 70), "\n\n")

# Meta-analysis for Total Accuracy
rma_total <- rma(yi = estimate, sei = std.error, data = coef_total, method = "REML")
cat("TOTAL ACCURACY:\n")
cat(sprintf("  Pooled effect: %.4f (95%% CI: %.4f to %.4f)\n",
            rma_total$b, rma_total$ci.lb, rma_total$ci.ub))
cat(sprintf("  p-value: %.4f\n", rma_total$pval))
cat(sprintf("  Heterogeneity: tau^2 = %.4f, I^2 = %.1f%%\n", rma_total$tau2, rma_total$I2))

# Meta-analysis for AI Detection (Fake)
rma_fake <- rma(yi = estimate, sei = std.error, data = coef_fake, method = "REML")
cat("\nAI DETECTION (FAKE CONTENT):\n")
cat(sprintf("  Pooled effect: %.4f (95%% CI: %.4f to %.4f)\n",
            rma_fake$b, rma_fake$ci.lb, rma_fake$ci.ub))
cat(sprintf("  p-value: %.4f\n", rma_fake$pval))
cat(sprintf("  Heterogeneity: tau^2 = %.4f, I^2 = %.1f%%\n", rma_fake$tau2, rma_fake$I2))

# Meta-analysis for Non-AI Accuracy (Real)
rma_real <- rma(yi = estimate, sei = std.error, data = coef_real, method = "REML")
cat("\nNON-AI ACCURACY (REAL CONTENT):\n")
cat(sprintf("  Pooled effect: %.4f (95%% CI: %.4f to %.4f)\n",
            rma_real$b, rma_real$ci.lb, rma_real$ci.ub))
cat(sprintf("  p-value: %.4f\n", rma_real$pval))
cat(sprintf("  Heterogeneity: tau^2 = %.4f, I^2 = %.1f%%\n", rma_real$tau2, rma_real$I2))

# =============================================================================
# 8. SESSION INFO
# =============================================================================

cat("\n\n", strrep("=", 70), "\n")
cat("SESSION INFO\n")
cat(strrep("=", 70), "\n\n")
sessionInfo()
