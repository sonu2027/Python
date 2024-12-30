# 1. Introduction to Pandas
import pandas as pd

# 2. Creating a DataFrame
# A DataFrame is a 2-dimensional labeled data structure, like a table in a database or an Excel spreadsheet. You can create a DataFrame from lists, dictionaries, or external data sources (like CSV files).
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [23, 34, 45, 36],
    'Score': [88, 92, 79, 85]
}

df = pd.DataFrame(data)
print(df)

# 3. Reading Data from a CSV File
# You can load external data from a CSV file into a Pandas DataFrame using pd.read_csv().
df = pd.read_csv('file.csv')
print(df.head())  # Print first 5 rows of the DataFrame

# 4. DataFrame Operations
# (A) Inspecting Data
# Displays the first few rows of the DataFrame
df.head()
# Displays the last few rows of the DataFrame
df.tail()

# Displays summary information about the DataFrame, like data types and non-null #values
df.info()

#  Generates descriptive statistics (mean, standard deviation, etc.) for numerical columns.
df.describe()

print(df.head())
print(df.info())
print(df.describe())

# (B) Selecting Data
# Selecting Columns: You can select a single column or multiple columns.
# Select a single column
age_column = df['Age']

# Select multiple columns
subset = df[['Name', 'Score']]
# Selecting Rows by Index: You can select rows by their index using .iloc[] (integer location) or .loc[] (label-based location).

# Select row by index
row = df.iloc[1]  # Select second row

# Select rows based on condition
subset = df[df['Age'] > 30]

# (C) Data Manipulation
# Adding a New Column
df['Status'] = ['Active', 'Inactive', 'Active', 'Inactive']

# Dropping a Column
df = df.drop('Status', axis=1)  # axis=1 specifies column, axis=0 is for rows

# Renaming Columns
df = df.rename(columns={'Age': 'Years'})

# (D) Sorting Data
# You can sort data by a column in either ascending or descending order.
df = df.sort_values(by='Age', ascending=False)  # Sort by Age in descending order

# (E) Grouping Data
# You can use groupby() to group data and perform aggregation functions like sum, mean, etc.
grouped = df.groupby('Status')['Score'].mean()  # Get average score by status
print(grouped)

# 5. Handling Missing Data
# You often encounter missing values (NaN) in real datasets. Pandas provides methods to handle them.
# Filling Missing Data
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill missing values with the mean

# Dropping Missing Data
df = df.dropna()  # Drop rows with any missing values