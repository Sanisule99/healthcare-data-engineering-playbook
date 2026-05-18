
import os
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

os.makedirs("06_imbalanced_medical_datasets/outputs", exist_ok=True)

rng = np.random.default_rng(42)
n = 500

df = pd.DataFrame({
    "feature_1": rng.normal(size=n),
    "feature_2": rng.normal(size=n),
    "rare_event": rng.binomial(1, 0.08, size=n)
})

X = df[["feature_1", "feature_2"]]
y = df["rare_event"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model = DummyClassifier(strategy="most_frequent")
model.fit(X_train, y_train)
pred = model.predict(X_test)

with open("06_imbalanced_medical_datasets/outputs/classification_report.txt", "w") as f:
    f.write(classification_report(y_test, pred, zero_division=0))

print("Saved imbalanced dataset report.")
