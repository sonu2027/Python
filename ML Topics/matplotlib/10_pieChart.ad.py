import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [40, 30, 20, 10]
colors = ['blue', 'green', 'red', 'purple']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Example')
plt.show()