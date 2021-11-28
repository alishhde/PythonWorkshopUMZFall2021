# Alishhde
import numpy as np

# Accessing element of 1-D array
arr = np.array([1, 2, 3, 4])
print(arr[0])

# Accessing element of 2-D array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])

# Accessing element of 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Negative indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Array Slicing 1-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[1:])
print(arr[:])
print(arr[-3:-1])
print(arr[::2])

# Array Slicing 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])