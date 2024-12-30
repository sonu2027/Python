import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]

plt.scatter(x, y, color='red', label="actual data")  # Scatter plot
plt.plot(x, y, color='blue', label="regression line")  # plot the graph
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.legend()
plt.show()