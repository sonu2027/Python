import pandas as pd

df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]}, index=[0, 1])
df2 = pd.DataFrame({'Score': [85, 90]}, index=[0, 1])

joined_df = df1.join(df2)
print(joined_df)
