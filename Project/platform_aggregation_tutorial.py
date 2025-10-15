# Load necessary packages
import pandas as pd

# Load the CSV file
platforms = pd.read_csv("policy_platforms.csv")

# Sort and group, then aggregate
platforms_sorted = platforms.sort_values(
    by=["candidate_webname", "state_postal", "cd", "cand_party", "year", "statement_id"]
)

# Group and summarize
platforms_agg = (
    platforms_sorted
    .groupby(["candidate_webname", "state_postal", "cd", "cand_party", "year"], as_index=False)
    .apply(lambda group: pd.Series({
        "platform_text": " ".join(f"{h}: {t}" for h, t in zip(group["issue_header"], group["issue_text"]))
    }))
    .reset_index(drop=True)
)

# Save resulting csv file
platforms_agg.to_csv('policy_platforms_aggregated.csv', index = False)
