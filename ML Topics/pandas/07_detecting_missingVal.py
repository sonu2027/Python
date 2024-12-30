# Detecting Missing Values

import pandas as pd
import numpy as np

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 30, 35],
        'Score': [85, 90, np.nan, 95]}

df = pd.DataFrame(data)
print(df)

# Finding Missing Values
# isna() or isnull() – Returns True for missing values and False otherwise.
print(df.isna())

# Count missing values:
print(df.isna().sum())

# Handling Missing Values
# (A) Removing Rows or Columns
# Remove rows with missing values:
df_dropped = df.dropna()
print(df_dropped)

# Remove columns with missing values:
df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols)

# (B) Filling Missing Values
# Fill with a specific value:
df_filled = df.fillna(0)
print(df_filled)


# Fill using mean:
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

# Replacing Specific Values
# Replace all NaN values with 'Unknown' in the 'Name' column:
df['Name'] = df['Name'].fillna('Unknown')
print(df)