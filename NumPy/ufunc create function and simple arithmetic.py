import numpy as np

# Create your own ufunc for addition
def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print("Custom ufunc myadd result:", myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a function is a ufunc
print("Type of np.add:", type(np.add))  # Should print <class 'numpy.ufunc'>
print("Type of np.concatenate:", type(np.concatenate))  # Not a ufunc


# Check with if statement
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')

# Arithmetic operations
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print("\n Addition:", newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print("\n Subtraction:", newarr)

newarr = np.multiply(arr1, arr2)
print("\n Multiplication:", newarr)

arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print("\n Division:", newarr)

arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print("\n Power:", newarr)

arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print("\n Modulus:", newarr)

newarr = np.remainder(arr1, arr2)
print("\n Remainder:", newarr)

newarr = np.divmod(arr1, arr2)
print("\n Divmod Quotients:", newarr[0])
print("\n Divmod Remainders:", newarr[1])

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print("\n Absolute:", newarr)
