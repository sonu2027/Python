import pandas as pd

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)
print(df)

print(df['Name'])  # Access 'Name' column
print(df.loc[0])  # Access row at index 0
print(df.loc[1, 'Age'])  # Access 'Age' of row 1

# Data manipulation
# adding column
df['Passed'] = [True, True, False]  # New column
print(df)

# sorting
sorted_df = df.sort_values('Score', ascending=False)  # Sort by Score
print(sorted_df)

# handling missing data
# A. Fill Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill NaN with mean

# B. Drop Rows with Missing Values
df = df.dropna()  # Remove rows with NaN values

# group and aggregation
grouped = df.groupby('Age')['Score'].mean()
print(grouped)

# From CSV file
# df = pd.read_csv('data.csv')  # Load data from a CSV file
# print(df.head())              # Display first 5 rows