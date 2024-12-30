import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Shape and size
print("Shape:", arr.shape)  # (2, 3)
print("Size:", arr.size)    # 6

# Access elements
print("Element at [0, 1]:", arr[0, 1])  # 2

# Slicing
print("First row:", arr[0])  # [1, 2, 3]
print("First column:", arr[:, 0])  # [1, 4]
