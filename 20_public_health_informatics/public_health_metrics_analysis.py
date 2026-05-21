import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "public_health_program_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Calculate measures safely
df["bp_screening_rate"] = df["screened_bp"] / df["total_participants"]
df["high_bp_identification_rate"] = df["high_bp_identified"] / df["screened_bp"]
df["referral_completion_rate"] = df["referrals_completed"] / df["high_bp_identified"]
df["followup_completion_rate"] = df["followup_completed"] / df["high_bp_identified"]

# Site-level summary
site_summary = (
    df.groupby("site_id")
    .agg(
        total_participants=("total_participants", "sum"),
        screened_bp=("screened_bp", "sum"),
        high_bp_identified=("high_bp_identified", "sum"),
        referrals_completed=("referrals_completed", "sum"),
        followup_completed=("followup_completed", "sum")
    )
    .reset_index()
)

site_summary["bp_screening_rate"] = site_summary["screened_bp"] / site_summary["total_participants"]
site_summary["referral_completion_rate"] = site_summary["referrals_completed"] / site_summary["high_bp_identified"]
site_summary["followup_completion_rate"] = site_summary["followup_completed"] / site_summary["high_bp_identified"]

# Equity stratification
equity_summary = (
    df.groupby("race_ethnicity")
    .agg(
        total_participants=("total_participants", "sum"),
        screened_bp=("screened_bp", "sum"),
        high_bp_identified=("high_bp_identified", "sum"),
        referrals_completed=("referrals_completed", "sum"),
        followup_completed=("followup_completed", "sum")
    )
    .reset_index()
)

equity_summary["bp_screening_rate"] = equity_summary["screened_bp"] / equity_summary["total_participants"]
equity_summary["referral_completion_rate"] = equity_summary["referrals_completed"] / equity_summary["high_bp_identified"]
equity_summary["followup_completion_rate"] = equity_summary["followup_completed"] / equity_summary["high_bp_identified"]

# Save outputs
df.to_csv(OUTPUT_DIR / "row_level_metrics.csv", index=False)
site_summary.to_csv(OUTPUT_DIR / "site_summary.csv", index=False)
equity_summary.to_csv(OUTPUT_DIR / "equity_summary.csv", index=False)

print("Public health metrics analysis complete.")
print("Outputs saved to:", OUTPUT_DIR)

print("\nSite Summary:")
print(site_summary)

print("\nEquity Summary:")
print(equity_summary)
