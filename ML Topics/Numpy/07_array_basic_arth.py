#  Basic Arithmetic

import numpy as np

arr = np.array([10, 20, 30])

# Addition
print(arr + 5)

# Multiplication
print(arr * 2)

# Square
print(arr ** 2)

print(arr.sum())
print(arr.mean())

print(arr.min())
print(arr.max())

#  slicing
print(arr[1:4])  # [20 30 40]

# accessing element
arr = np.array([10, 20, 30, 40, 50])
print(arr[1])   # 20
print(arr[-1])  # 50

# reshaping array
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)  # 2 rows, 3 columns
print(reshaped)