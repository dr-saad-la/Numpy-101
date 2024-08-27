import numpy as np

arr_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr_from_list)

arr_arange = np.arange(10)
print("Array using arange():", arr_arange)

arr_zeros = np.zeros(5)
print("Array of zeros:", arr_zeros)

arr_ones = np.ones(5)
print("Array of ones:", arr_ones)

arr_linspace = np.linspace(0, 1, 5)
print("Array using linspace():", arr_linspace)

arr_random = np.random.randint(1, 10, 5)
print("Array of random integers:", arr_random)