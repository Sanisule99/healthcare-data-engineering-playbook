import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "tile_metadata_example.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Summarize tile-level predictions by slide
slide_summary = (
    df.groupby("slide_id")
    .agg(
        total_tiles=("tile_id", "count"),
        avg_tissue_percent=("tissue_percent", "mean"),
        avg_prediction_probability=("prediction_probability", "mean"),
        tumor_tile_count=("predicted_class", lambda x: (x == "tumor").sum()),
        benign_tile_count=("predicted_class", lambda x: (x == "benign").sum())
    )
    .reset_index()
)

slide_summary["tumor_tile_fraction"] = (
    slide_summary["tumor_tile_count"] / slide_summary["total_tiles"]
)

slide_summary["slide_level_prediction"] = slide_summary["tumor_tile_fraction"].apply(
    lambda x: "tumor" if x >= 0.5 else "benign"
)

slide_summary.to_csv(OUTPUT_DIR / "slide_level_summary.csv", index=False)

print("Digital pathology tile summary complete.")
print(slide_summary)
print("Saved to:", OUTPUT_DIR / "slide_level_summary.csv")
