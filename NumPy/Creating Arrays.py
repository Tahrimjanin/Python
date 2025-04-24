import numpy as np

#0-D Arrays
arr = np.array(42)
print(arr)

#1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print("\n")
print(arr)

#2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\n")
print(arr)

#3-D arrays
print("\n")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

#Check Number of Dimensions 
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("\n")
print(a.ndim) #ndim for dimantion number 
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher Dimensional Arrays

print("\n")
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)