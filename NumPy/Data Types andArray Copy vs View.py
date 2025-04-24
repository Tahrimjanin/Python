import numpy as np
# Basic NumPy dtypes

print(" Checking Data Types")
arr1 = np.array([1, 2, 3, 4])
print("arr1 dtype:", arr1.dtype)

arr2 = np.array(['apple', 'banana', 'cherry'])
print("arr2 dtype:", arr2.dtype)

# Creating Arrays With Defined Data Types
print("\nCreating Arrays with Specific Data Types")
arr3 = np.array([1, 2, 3, 4], dtype='S')
print("arr3:", arr3)
print("arr3 dtype:", arr3.dtype)

arr4 = np.array([1, 2, 3, 4], dtype='i4')
print("arr4:", arr4)
print("arr4 dtype:", arr4.dtype)

# Converting Data Types with astype()

print("\nConverting Data Types")
arr5 = np.array([1.1, 2.1, 3.1])
newarr1 = arr5.astype('i')
print("Converted to int using 'i':", newarr1, newarr1.dtype)

newarr2 = arr5.astype(int)
print("Converted to int using int:", newarr2, newarr2.dtype)

arr6 = np.array([1, 0, 3])
newarr3 = arr6.astype(bool)
print("Converted to bool:", newarr3, newarr3.dtype)


# Copy vs View

print("\nCopy vs View")
arr7 = np.array([1, 2, 3, 4, 5])

# Copy
copy_arr = arr7.copy()
arr7[0] = 42
print("Original after change:", arr7)
print("Copy remains unchanged:", copy_arr)

# View
arr8 = np.array([1, 2, 3, 4, 5])
view_arr = arr8.view()
arr8[0] = 42
print("Original changed:", arr8)
print("View reflects change:", view_arr)

# Change view and show original affected
view_arr[1] = 99
print("View modified:", view_arr)
print("Original also affected:", arr8)

# Check Ownership

print("\nCheck Ownership with .base ")
print("copy_arr.base:", copy_arr.base)  
print("view_arr.base:", view_arr.base) 