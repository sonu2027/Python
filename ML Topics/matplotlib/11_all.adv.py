# 1. Importing Matplotlib
import matplotlib.pyplot as plt

# 2. Basic Plotting
# (A) Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 3. Bar Plot
x = ['A', 'B', 'C', 'D']
y = [3, 7, 4, 8]
plt.bar(x, y)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 4. Scatter Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 5. Histogram
data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
plt.hist(data, bins=5, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 6. Pie Chart
labels = ['Python', 'Java', 'C', 'JavaScript']
sizes = [40, 30, 20, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()

# 7. Subplots
# (A) Multiple Plots in One Figure
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
fig, axes = plt.subplots(2, 2)  # 2x2 grid of subplots
axes[0, 0].plot(x, y)
axes[0, 0].set_title('Line Plot')
axes[0, 1].bar(x, y)
axes[0, 1].set_title('Bar Plot')
axes[1, 0].scatter(x, y)
axes[1, 0].set_title('Scatter Plot')
axes[1, 1].pie(y, labels=x, autopct='%1.1f%%')
axes[1, 1].set_title('Pie Chart')
plt.tight_layout()  # Adjust spacing between subplots
plt.show()

# 8. Customizing Plots
# (A) Adding Gridlines
plt.plot(x, y)
plt.grid(True)  # Show grid
plt.show()

# (B) Customizing Color, Line Style, and Markers
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title('Customized Line Plot')
plt.show()