import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    precision_recall_curve,
    auc
)

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "imbalanced_health_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

features = [
    "age",
    "prior_encounters",
    "chronic_condition_count",
    "abnormal_lab_flag"
]

target = "rare_event"

X = df[features]
y = df[target]

print("Outcome distribution:")
print(y.value_counts(normalize=True))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    max_depth=4
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
report_df.to_csv(OUTPUT_DIR / "classification_report.csv")

cm = confusion_matrix(y_test, y_pred)
pd.DataFrame(
    cm,
    index=["Actual_0", "Actual_1"],
    columns=["Predicted_0", "Predicted_1"]
).to_csv(OUTPUT_DIR / "confusion_matrix.csv")

roc_auc = roc_auc_score(y_test, y_prob)

precision, recall, _ = precision_recall_curve(y_test, y_prob)
pr_auc = auc(recall, precision)

importance_df = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

importance_df.to_csv(OUTPUT_DIR / "feature_importance.csv", index=False)

plt.figure(figsize=(7, 5))
plt.barh(importance_df["feature"], importance_df["importance"])
plt.xlabel("Feature Importance")
plt.title("Feature Importance — Imbalanced Medical Dataset")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "feature_importance.png", dpi=300)

summary = pd.DataFrame({
    "metric": ["roc_auc", "pr_auc", "positive_event_rate"],
    "value": [roc_auc, pr_auc, y.mean()]
})

summary.to_csv(OUTPUT_DIR / "model_summary.csv", index=False)

print("Modeling complete.")
print("ROC AUC:", round(roc_auc, 3))
print("PR AUC:", round(pr_auc, 3))
print("Outputs saved to:", OUTPUT_DIR)
