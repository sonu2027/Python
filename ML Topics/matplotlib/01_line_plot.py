import matplotlib.pyplot as plt

# Data
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

# Plotting the data
plt.plot(b, a)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')

# Display the plot
plt.show()
