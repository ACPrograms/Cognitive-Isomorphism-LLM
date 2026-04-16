from datasets import load_dataset
import pandas as pd

print("Downloading dataset...")
# Using a valid dedicated Kabyle-French dataset
dataset = load_dataset("Sifal/Kabyle-French", split="train")

df = pd.DataFrame(dataset)

# Handle both flat and nested 'translation' structures dynamically
if 'translation' in df.columns and len(df.columns) == 1:
    df_cleaned = df['translation'].apply(pd.Series).dropna().head(6600)
else:
    df_cleaned = df.dropna().head(6600)

# Export to CSV
output_filename = "tamazight_french_6600.csv"
df_cleaned.to_csv(output_filename, index=False)

print(f"Phase 1 Complete: {len(df_cleaned)} parallel tokens saved to {output_filename}.")
print("Columns saved:", list(df_cleaned.columns))