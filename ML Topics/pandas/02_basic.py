import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Display data
print("DataFrame:")
print(df)

# Access a column
print("\nNames:")
print(df['Name'])

# Filter rows
print("\nFiltered Rows:")
print(df[df['Age'] > 25])