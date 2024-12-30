import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
import pandas as pd
data = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [10, 15, 20, 25, 30]})

# Seaborn scatter plot
sns.scatterplot(x='X', y='Y', data=data)

plt.title('Seaborn Scatter Plot')
plt.show()
