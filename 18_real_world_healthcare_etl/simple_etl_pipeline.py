import pandas as pd
from pathlib import Path

input_path = Path('datasets/sample-data/patients.csv')
output_path = Path('18_real_world_healthcare_etl/clean_patients.csv')

df = pd.read_csv(input_path)
df.columns = [c.lower().strip() for c in df.columns]
df = df.drop_duplicates()

output_path.parent.mkdir(exist_ok=True)
df.to_csv(output_path, index=False)

print('Saved cleaned file:', output_path)
