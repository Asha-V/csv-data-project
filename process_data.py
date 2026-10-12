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
# Update sample passenger names and IDs
changes = {
    887: {"PassengerId": 1001, "Name": "Asha Demo"},
    888: {"PassengerId": 1002, "Name": "Data User One"},
    889: {"PassengerId": 1003, "Name": "Data User Two"}
}

for old_id, values in changes.items():
    matching_rows = df["PassengerId"] == old_id
    df.loc[matching_rows, "Name"] = values["Name"]
    df.loc[matching_rows, "PassengerId"] = values["PassengerId"]

# Verify the changes
print("\nUpdated sample records:")
print(df[df["PassengerId"].isin([1001, 1002, 1003])])
print("Duplicate IDs:", df["PassengerId"].duplicated().sum())

# Convert to different formats
df.to_csv("cleaned_titanic.csv", index=False)
df.to_json("cleaned_titanic.json", orient="records", indent=2)
df.to_parquet("cleaned_titanic.parquet", index=False)

print("\nCleaning completed.")
print("CSV, JSON, and Parquet files created.")
