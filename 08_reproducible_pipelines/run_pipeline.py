import json
import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent

def log(message, log_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def load_config():
    with open(BASE_DIR / "config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def validate_columns(df, required_columns):
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def run_pipeline():
    config = load_config()

    input_path = BASE_DIR / config["input_file"]
    output_path = BASE_DIR / config["output_file"]
    log_path = BASE_DIR / config["log_file"]

    output_path.parent.mkdir(exist_ok=True)
    log_path.parent.mkdir(exist_ok=True)

    log("Pipeline started", log_path)

    df = pd.read_csv(input_path)
    log(f"Loaded input file with shape: {df.shape}", log_path)

    df.columns = [c.lower().strip() for c in df.columns]
    validate_columns(df, config["required_columns"])
    log("Required columns validated", log_path)

    df = df.drop_duplicates()
    log(f"After duplicate removal: {df.shape}", log_path)

    df["high_utilization_flag"] = (
        df["encounter_count"] >= config["high_utilization_threshold"]
    ).astype(int)

    df["multiple_chronic_conditions_flag"] = (
        df["chronic_condition_count"] >= config["high_chronic_condition_threshold"]
    ).astype(int)

    df["risk_score"] = (
        df["high_utilization_flag"]
        + df["multiple_chronic_conditions_flag"]
        + (df["age"] >= 65).astype(int)
    )

    df.to_csv(output_path, index=False)
    log(f"Saved processed output to: {output_path}", log_path)

    log("Pipeline completed successfully", log_path)

if __name__ == "__main__":
    run_pipeline()
