import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "synthetic_risk_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

features = [
    "age",
    "prior_encounters",
    "chronic_condition_count",
    "abnormal_lab_flag",
    "medication_count"
]

target = "high_risk"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    max_depth=3
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
report_df.to_csv(OUTPUT_DIR / "classification_report.csv")

auc = roc_auc_score(y_test, y_prob)

importance_df = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

importance_df.to_csv(OUTPUT_DIR / "feature_importance.csv", index=False)

plt.figure(figsize=(8, 5))
plt.barh(
    importance_df["feature"],
    importance_df["importance"]
)
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Healthcare Risk Model Feature Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "feature_importance.png", dpi=300)

print("Model complete.")
print(f"ROC AUC: {auc:.3f}")
print("Outputs saved to:", OUTPUT_DIR)
print(importance_df)
