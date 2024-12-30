import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise operations
print("Addition:", arr1 + arr2)  # [5, 7, 9]
print("Multiplication:", arr1 * arr2)  # [4, 10, 18]

# Matrix multiplication
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
result = np.dot(arr3, arr4)
print("Matrix Multiplication:\n", result)
