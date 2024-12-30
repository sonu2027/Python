import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 90, 75]})

# Merging based on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID')

print(merged_df)


# Types of Joins in merge()
# Join Type	Description	Example Syntax
# Inner Join	Keeps rows where keys match in both DataFrames (default).	pd.merge(df1, df2, on='ID', how='inner')
# Left Join	Keeps all rows from the left DataFrame and matches from the right.	pd.merge(df1, df2, on='ID', how='left')
# Right Join	Keeps all rows from the right DataFrame and matches from the left.	pd.merge(df1, df2, on='ID', how='right')
# Outer Join	Keeps all rows from both DataFrames, filling missing values with NaN.	pd.merge(df1, df2, on='ID', how='outer')