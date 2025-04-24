import numpy as np

print("SPLITTING ARRAYS ")
arr1 = np.array([1, 2, 3, 4, 5, 6])
split_arr1 = np.array_split(arr1, 3)
print("\n Split into 3 parts:", split_arr1)

arr2D = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]])
split_arr2D = np.array_split(arr2D, 3)
print("2D split (axis=0):", split_arr2D)

split_arr2D_axis1 = np.array_split(arr2D, 3, axis=1)
print("2D split (axis=1):", split_arr2D_axis1)

hsplit_arr = np.hsplit(arr2D, 3)
print("2D split using hsplit():", hsplit_arr)

print("\nSEARCHING ARRAYS ")
arr_search = np.array([1, 2, 3, 4, 5, 4, 4])
indices_4 = np.where(arr_search == 4)
print("Indices where value is 4:", indices_4)

even_indices = np.where(arr_search % 2 == 0)
print("Even number indices:", even_indices)

odd_indices = np.where(arr_search % 2 == 1)
print("Odd number indices:", odd_indices)

sorted_arr = np.array([6, 7, 8, 9])
insert_index = np.searchsorted(sorted_arr, 7)
print("Searchsorted index for 7:", insert_index)

insert_index_right = np.searchsorted(sorted_arr, 7, side='right')
print("Searchsorted index for 7 from right:", insert_index_right)

multi_insert_index = np.searchsorted(np.array([1, 3, 5, 7]), [2, 4, 6])
print("Indexes for inserting 2, 4, 6:", multi_insert_index)

print("\nSORTING ARRAYS ")
arr_sort1 = np.array([3, 2, 0, 1])
print("Sorted array:", np.sort(arr_sort1))

arr_sort2 = np.array(['banana', 'cherry', 'apple'])
print("Sorted strings:", np.sort(arr_sort2))

arr_sort3 = np.array([True, False, True])
print("Sorted boolean:", np.sort(arr_sort3))

arr_sort2D = np.array([[3, 2, 4], [5, 0, 1]])
print("Sorted 2D array:\n", np.sort(arr_sort2D))

print("\nFILTERING ARRAYS ")
arr_filter = np.array([41, 42, 43, 44])
bool_filter = [True, False, True, False]
filtered_arr_manual = arr_filter[bool_filter]
print("Filtered manually (index 0 and 2):", filtered_arr_manual)

# Filter values > 42 using loop
filter_arr_loop = []
for val in arr_filter:
    filter_arr_loop.append(val > 42)

filtered_arr_loop = arr_filter[filter_arr_loop]
print("Filtered > 42 using loop:", filtered_arr_loop)

# Direct NumPy filter
filtered_arr_direct = arr_filter[arr_filter > 42]
print("Filtered > 42 using direct NumPy:", filtered_arr_direct)

# Filter even numbers
arr_even = np.array([1, 2, 3, 4, 5, 6, 7])
filtered_even = arr_even[arr_even % 2 == 0]
print("Filtered even numbers:", filtered_even)
