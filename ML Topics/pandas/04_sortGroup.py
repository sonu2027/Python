import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Score': [80, 90, 85, 70]}

df = pd.DataFrame(data)

# Sort by Age
sorted_df = df.sort_values(by='Age')

# Group by Name and calculate mean
grouped_df = df.groupby('Name')['Score'].mean()

print("Sorted DataFrame:\n", sorted_df)
print("\nGrouped DataFrame:\n", grouped_df)
