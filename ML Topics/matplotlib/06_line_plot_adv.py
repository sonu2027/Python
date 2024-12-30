import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, marker='o', color='b', linestyle='--', label='Line 1')  # Line plot
plt.title('Line Plot Example')    # Title
plt.xlabel('X-axis')             # X-axis label
plt.ylabel('Y-axis')             # Y-axis label
plt.legend()                     # Legend
plt.grid(True)                   # Grid lines
plt.show()                       # Display the plot