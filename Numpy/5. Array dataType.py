# Alishhde
import numpy as np

# Let's see array's datatype
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Create an array with defined datatype
arr = np.array([1, 2, 3, 4], ndmin=2, dtype='f')
print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(arr.dtype)
print(newarr.dtype)