import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

#  mean (avarage)
x = np.mean(speed)
print(f"Mean: {x}")

#  median (middle value)
y = np.median(speed)
print(f"Median: {y}")

# mode (most common value) _Scipy
z = stats.mode(speed)
print(f"Mode: {z.mode[0]}")  

# Speed data
speed = [32, 111, 138, 28, 59, 77, 97]

# Calculating Mean
mean = np.mean(speed)
print(f"Mean: {mean}")

# Calculating Variance
variance = np.var(speed)
print(f"Variance: {variance}")

# Calculating Standard Deviation
std_dev = np.std(speed)
print(f"Standard Deviation: {std_dev}")

# Verifying relationship between variance and standard deviation
std_dev_calculated_from_variance = np.sqrt(variance)
print(f"Standard Deviation from Variance: {std_dev_calculated_from_variance}")
