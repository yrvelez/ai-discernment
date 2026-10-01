# =============================================================================
# Create Replication Data
# =============================================================================
# Run this ONCE to generate replication_data.csv from raw Qualtrics export
# =============================================================================

library(tidyverse)

# Load raw data (skip Qualtrics header rows)
raw_data <- read_csv("raw_data/Improving+AI+Discernment_January+16,+2026_10.49.csv", skip = 2)

# Remove PII columns (but keep a pseudonymized participant_id for clustering)
pii_cols <- c(
  "IPAddress", "ResponseId", "RecipientLastName", "RecipientFirstName",
  "RecipientEmail", "ExternalReference", "LocationLatitude", "LocationLongitude",
  "assignmentId", "projectId"
)

replication_data <- raw_data %>%
  # Create pseudonymized participant ID (hash the original, then convert to integer)
  mutate(participant_id = as.integer(factor(participantId))) %>%
  select(-any_of(pii_cols), -participantId)  # Remove original participantId after creating pseudo ID

write_csv(replication_data, "data/replication_data.csv")
cat("Saved replication_data.csv:", nrow(replication_data), "rows,", ncol(replication_data), "columns\n")
