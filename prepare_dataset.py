
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
input_file = BASE_DIR / "data" / "deceptive-opinion.csv"
output_file = BASE_DIR / "data" / "reviews_1000.csv"

# Read original dataset
df = pd.read_csv(input_file)

# Keep only required columns
df = df[["text", "deceptive"]].copy()

# Convert labels
df["deceptive"] = df["deceptive"].map({
    "truthful": "genuine",
    "deceptive": "fake"
})

# Rename columns
df = df.rename(columns={
    "text": "review",
    "deceptive": "label"
})

# Remove missing and duplicate reviews
df = df.dropna(subset=["review", "label"])
df = df.drop_duplicates(subset=["review"])

# Select 500 reviews from each class
genuine = df[df["label"] == "genuine"].sample(
    n=500, random_state=42
)

fake = df[df["label"] == "fake"].sample(
    n=500, random_state=42
)

# Combine and shuffle
final_df = pd.concat([genuine, fake])
final_df = final_df.sample(frac=1, random_state=42)

# Save new dataset
final_df.to_csv(output_file, index=False)

print("Dataset created successfully!")
print("Total Reviews:", len(final_df))
print(final_df["label"].value_counts())
print("Saved to:", output_file)
