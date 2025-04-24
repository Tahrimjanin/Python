#Slicing arrays==taking elements from one given index to another given index.

import numpy as np

arr1d = np.array([1, 2, 3, 4, 5, 6, 7])

# 1. Slice from index 1 to index 5 =
print("Slice 1 to 5:", arr1d[1:5])  # Output: [2 3 4 5]

# 2. Slice from index 4 to the end
print("Slice 4 to end:", arr1d[4:])  

# 3. Slice from beginning to index 4 (not included)
print("Slice beginning to 4:", arr1d[:4])  

# 4. Negative slicing: index -3 to -1 (not included)
print("Negative slice -3 to -1:", arr1d[-3:-1])  

# 5. Step slicing: every other element from index 1 to 5
print("Step slice 1 to 5, step 2:", arr1d[1:5:2])  

# 6. Step slicing: every other element in the whole array
print("Step slice whole array, step 2:", arr1d[::2]) 

# Create a 2D array for 2D examples
arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# 7. From the second row, slice elements from index 1 to 4 (not included)
print("2D slice row 1, cols 1 to 4:", arr2d[1, 1:4]) 

# 8. From both rows, get index 2 (column)
print("2D slice both rows, col 2:", arr2d[0:2, 2]) 

# 9. From both rows, slice columns 1 to 4 (not included)
print("2D slice both rows, cols 1 to 4:\n", arr2d[0:2, 1:4])
