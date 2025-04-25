import numpy as np

# Sample data
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# Standard Deviation measures how spread out the values in a data set are
std_dev = np.std(ages)
print("Standard Deviation:", std_dev)

# Percentiles (75th and 90th) -The value below which a given percentage of the data falls.
percentile_75 = np.percentile(ages, 75)
percentile_90 = np.percentile(ages, 90)


print("75th Percentile:", percentile_75)
print("90th Percentile:", percentile_90)
