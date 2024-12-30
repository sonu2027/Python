# 1. Installing Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# 3. Basic Plotting with Seaborn
# (A) Distribution Plot (Histogram)
import numpy as np
data = np.random.randn(100)  # 100 random numbers from a normal distribution
sns.histplot(data, kde=True)  # Histogram with KDE (Kernel Density Estimate)
plt.title('Distribution Plot')
plt.show()

# (B) Box Plot
# Box plot shows the distribution of data based on quartiles
data = [np.random.rand(100) for _ in range(5)]  # 5 different datasets
sns.boxplot(data=data)
plt.title('Box Plot')
plt.show()

# (C) Bar Plot
data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 20, 30, 40]}
sns.barplot(x='Category', y='Values', data=data)
plt.title('Bar Plot')
plt.show()

# (D) Heatmap
# A heatmap shows the correlation matrix of a dataset or any other 2D data structure.
import numpy as np
data = np.random.rand(10, 12)  # Random data in 10x12 matrix
sns.heatmap(data, annot=True, cmap='coolwarm')  # annot=True adds numbers inside the heatmap cells
plt.title('Heatmap')
plt.show()

# 4. Pair Plot
# A pair plot shows relationships between variables in a dataset by plotting all pairwise combinations of numeric features.
# Using built-in Seaborn dataset 'iris'
sns.pairplot(sns.load_dataset('iris'))
plt.title('Pair Plot')
plt.show()

# 5. Violin Plot
# A violin plot combines aspects of boxplot and KDE, showing the distribution of data and its probability density.
data = sns.load_dataset('tips')
sns.violinplot(x='day', y='total_bill', data=data)
plt.title('Violin Plot')
plt.show()

# 6. Customizing Seaborn Plots
# You can use sns.set() to set the default style of your plots.
sns.set(style="whitegrid")  # Change plot style to a white grid background

# Now, create any plot and it will use the whitegrid style
sns.barplot(x='Category', y='Values', data=data)
plt.show()