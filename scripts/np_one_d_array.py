import numpy as np

# 1. Creating a NumPy array from a Python list
# This converts a regular Python list into a NumPy array.
array_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", array_from_list)
# Output: Array from list: [1 2 3 4 5]

# 2. Creating a NumPy array using arange()
# arange() generates an array of evenly spaced values within a given range.
# Here, it creates an array of integers from 0 to 9.
array_arange = np.arange(10)
print("Array using arange():", array_arange)
# Output: Array using arange(): [0 1 2 3 4 5 6 7 8 9]

# 3. Creating a NumPy array of zeros
# zeros() creates an array filled with zeros.
# The argument specifies the length of the array.
array_zeros = np.zeros(5)
print("Array of zeros:", array_zeros)
# Output: Array of zeros: [0. 0. 0. 0. 0.]

# 4. Creating a NumPy array of ones
# ones() creates an array filled with ones.
# The argument specifies the length of the array.
array_ones = np.ones(5)
print("Array of ones:", array_ones)
# Output: Array of ones: [1. 1. 1. 1. 1.]

# 5. Creating a NumPy array with a specific range and step using linspace()
# linspace() generates a specified number of evenly spaced values over a defined interval.
# Here, it generates 5 numbers evenly spaced between 0 and 1.
array_linspace = np.linspace(0, 1, 5)
print("Array using linspace():", array_linspace)
# Output: Array using linspace(): [0.   0.25 0.5  0.75 1.  ]

# 6. Creating a NumPy array using random integers
# random.randint() generates random integers within a specified range.
# Here, it creates an array of 5 random integers between 1 and 10.
array_random = np.random.randint(1, 10, 5)
print("Array of random integers:", array_random)
# Output: Array of random integers: [9 3 6 2 7]