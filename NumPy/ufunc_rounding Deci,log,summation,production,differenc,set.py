import numpy as np

arr = np.array([-3.1666, 3.6667])

print("Original array:", arr)

#1.Rounding Decimals
# Truncate (remove decimal part)
trunc_result = np.trunc(arr)
print("np.trunc():", trunc_result)

# Fix (round towards zero)
fix_result = np.fix(arr)
print("np.fix():", fix_result)

# Around (round to given decimals)
around_result = np.around(arr, 2)
print("np.around():", around_result)

# Floor (round down)
floor_result = np.floor(arr)
print("np.floor():", floor_result)

# Ceil (round up)
ceil_result = np.ceil(arr)
print("np.ceil():", ceil_result)


#2.Logarithm (base e)
log_result = np.log([1, np.e, 10])
print("np.log():", log_result)


#3,Summation 
sum_result = np.sum(arr)
print("np.sum():", sum_result)


# 4.Production
prod_result = np.prod(arr)
print("np.prod():", prod_result)


#5. Difference between elements
diff_result = np.diff(arr)
print("np.diff():", diff_result)


#6. Set operations
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_result = np.union1d(set1, set2)
print("Union:", union_result)

# Intersection
intersection_result = np.intersect1d(set1, set2)
print("Intersection:", intersection_result)

# Difference 
difference_result = np.setdiff1d(set1, set2)
print("Set difference (set1 - set2):", difference_result)

# Symmetric difference
sym_diff_result = np.setxor1d(set1, set2)
print("Symmetric difference:", sym_diff_result)
