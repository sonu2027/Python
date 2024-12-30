import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [10, 20, 30, 40]

plt.bar(x, y, color='green')  # Bar chart
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

plt.show()
