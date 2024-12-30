import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', np.nan],
        'Age': [25, np.nan, 30],
        'Salary': [50000, 60000, 70000]}

df = pd.DataFrame(data)
print("data frame: \n", df)
# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean()) # fillna fill the missing value

print("After Filling Missing Data:")
print(df)