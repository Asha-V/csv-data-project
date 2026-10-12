import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

# Inspect columns and data types
print("Columns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Clean the dataset
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Convert to different formats
df.to_csv("cleaned_titanic.csv", index=False)
df.to_json("cleaned_titanic.json", orient="records", indent=2)
df.to_parquet("cleaned_titanic.parquet", index=False)

print("\nCleaning completed.")
print("CSV, JSON, and Parquet files created.")
