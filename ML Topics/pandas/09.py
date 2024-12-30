import pandas as pd

# 2. Creating DataFrames
# (A) From a Dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# 3. Viewing Data
print(df.head())    # First 5 rows
print(df.tail())    # Last 5 rows
print(df.info())    # Summary of the DataFrame
print(df.describe())# Statistics summary

# 4. Selecting Data
# (A) Single Column
print(df['Name'])

# (B) Multiple Columns
print(df[['Name', 'Age']])
# (C) Rows using iloc
print(df.iloc[0])  # First row
print(df.iloc[0:2]) # First two rows

# (D) Rows using loc
print(df.loc[0, 'Name'])  # Value at row 0, column 'Name'

# 5. Filtering Data
print(df[df['Age'] > 25])  # Rows where Age > 25

# 6. Modifying Data
# (A) Add Column
df['Salary'] = [50000, 60000, 70000]
print(df)

# (B) Update Values
df.loc[0, 'Age'] = 26
print(df)

# (C) Drop Column
df = df.drop('City', axis=1)  # Drop 'City' column
print(df)

# 7. Handling Missing Values
# (A) Check Missing Values
print(df.isnull())
print(df.isnull().sum())

# (B) Fill Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 8. Sorting Data
print(df.sort_values(by='Age'))  # Sort by Age in ascending order
print(df.sort_values(by='Age', ascending=False))  # Descending order

# 9. Grouping Data
grouped_df = df.groupby('Age')['Salary'].mean()  # Average salary by age
print(grouped_df)

# 10. Reading and Writing CSV Files
# (A) Read CSV
# df = pd.read_csv('data.csv')

# (B) Write CSV
# df.to_csv('output.csv', index=False)