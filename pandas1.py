import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Bob"],
    "Age": [24, 27, None, 27],
    "City": ["New York", "Los Angeles", "Chicago", "Los Angeles"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Handling missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Removing duplicate rows
df = df.drop_duplicates()

# Renaming a column
df = df.rename(columns={"City": "Location"})

# Filtering data
filtered_df = df[df["Age"] > 25]

print("\nCleaned DataFrame:")
print(df)

print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)
print (df)
