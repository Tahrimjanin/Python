import numpy as np

# Shape of Arrays
print("1. Shape of Arrays")
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Array:\n", arr2d)
print("Shape:", arr2d.shape)

# Creating array with 5 dimensions
print("\n2. Array with 5 Dimensions")
arr5d = np.array([1, 2, 3, 4], ndmin=5)
print("Array:\n", arr5d)
print("Shape:", arr5d.shape)

# Reshaping arrays
print("\n3. Reshape from 1D to 2D")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2d_reshaped = arr1.reshape(4, 3)
print(arr2d_reshaped)

print("\n4. Reshape from 1D to 3D")
arr3d_reshaped = arr1.reshape(2, 3, 2)
print(arr3d_reshaped)

# Unknown dimension (-1)
print("\n5. Unknown Dimension")
arr_unknown = arr1.reshape(2, 2, -1)
print(arr_unknown)

# Flattening
print("\n6. Flattening")
arr_flat = arr2d.reshape(-1)
print(arr_flat)

# Iteration over 1D
print("\n7. Iterating 1D Array")
for x in arr1[:3]:
    print(x)

# Iteration over 2D
print("\n8. Iterating 2D Array")
for row in arr2d:
    for val in row:
        print(val)

# Iteration over 3D using nditer
print("\n9. Iterating 3D with nditer")
for x in np.nditer(arr3d_reshaped):
    print(x)

# Iterating with data type conversion
print("\n10. Iterating with dtype=str")
for x in np.nditer(arr1[:3], flags=['buffered'], op_dtypes=['S']):
    print(x)

# Enumerated iteration
print("\n11. Enumerated Iteration (2D array)")
for idx, val in np.ndenumerate(arr2d):
    print(idx, val)

# Joining arrays
print("\n12. Joining Arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
joined = np.concatenate((a, b))
print(joined)

# Joining 2D along rows
print("\n13. Joining 2D Arrays (axis=1)")
a2 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
joined2d = np.concatenate((a2, b2), axis=1)
print(joined2d)

# Stacking arrays
print("\n14. Stacking Arrays (axis=1)")
stacked = np.stack((a, b), axis=1)
print(stacked)

# Horizontal Stack
print("\n15. Horizontal Stack")
print(np.hstack((a, b)))

# Vertical Stack
print("\n16. Vertical Stack")
print(np.vstack((a, b)))

# Depth Stack
print("\n17. Depth Stack")
print(np.dstack((a, b)))
