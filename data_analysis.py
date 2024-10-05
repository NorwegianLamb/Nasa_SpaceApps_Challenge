import os
import pandas as pd

file_path = "./gii_countries.csv"
try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # or try 'latin1'
except Exception as e:
    print(f"Error reading the CSV file: {e}")

# Filter the DataFrame to keep only the desired columns
# Specify the columns you want to keep
columns_to_keep = ['iso3', 'country', 'hdicode'] + [f'gii_{year}' for year in range(1990, 2023)]

# Create a new DataFrame with only the specified columns
filtered_df = df[columns_to_keep]

# Display the filtered DataFrame
print(filtered_df)
print(df.columns)