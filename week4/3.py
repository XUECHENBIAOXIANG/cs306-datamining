import pandas as pd

# Load the dataset
df = pd.read_csv("Reviews.csv")

# Calculate the length of the original dataset
original_length = len(df)

# Deduplicate the dataset based on all columns
deduplicated_df = df.drop_duplicates()

# Calculate the length of the deduplicated dataset
deduplicated_length = len(deduplicated_df)

# Calculate the percentage of data retained after deduplication
percentage_retained = (deduplicated_length / original_length) * 100

print("Percentage of data retained after deduplication:", percentage_retained)
