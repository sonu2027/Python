import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, color='purple')  # Histogram
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Example')

plt.show()
