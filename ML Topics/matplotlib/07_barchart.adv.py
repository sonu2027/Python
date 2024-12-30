import matplotlib.pyplot as plt

products = ['Pen', 'Pencil', 'Eraser']
prices = [10, 5, 3]

plt.bar(products, prices, color='green')  # Bar chart
plt.title('Product Prices')
plt.xlabel('Products')
plt.ylabel('Prices')
plt.show()
