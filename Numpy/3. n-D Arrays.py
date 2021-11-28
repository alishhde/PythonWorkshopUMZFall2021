# Alishhde

import numpy as np

# 0-D Arrays -- 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr = np.array(100)
print(arr)
print('number of dimensions :', arr.ndim)

# 1-D Arrays -- An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print('number of dimensions :', arr.ndim)

# 2-D Arrays -- An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
arr = np.array([[1, 2], [3, 4]])
print(arr)
print('number of dimensions :', arr.ndim)

# 3-D Arrays -- An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.
arr = np.array([[[1, 2, 3, 4], [4, 5, 6, 7]], [[1, 2, 3, 4], [4, 5, 6, 7]]])
print(arr)
print('number of dimensions :', arr.ndim)

# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('Number of dimensions :', arr.ndim)

