import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(18, 5)) 

# 1. Create an array with 250 random floats between 0 and 5 (Uniform Distribution)
x_uniform = np.random.uniform(0.0, 5.0, 250)

# Plotting the histogram for uniform distribution (250 values)
plt.subplot(1, 3, 1)  # (rows, columns, index)
plt.hist(x_uniform, 5)
plt.title("Uniform Distribution (250 values)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

# 2. Create an array with 100,000 random floats between 0 and 5 (Uniform Distribution)
x_uniform_large = np.random.uniform(0.0, 5.0, 100000)

# Plotting the histogram for uniform distribution (100,000 values)
plt.subplot(1, 3, 2)
plt.hist(x_uniform_large, 100)
plt.title("Uniform Distribution (100,000 values)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

# 3. Create a normal distribution (mean = 5.0, std dev = 1.0, size = 100,000)
x_normal = np.random.normal(5.0, 1.0, 100000)

# Plotting the histogram for normal distribution
plt.subplot(1, 3, 3)
plt.hist(x_normal, 100)
plt.title("Normal Distribution (100,000 values)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.tight_layout()  # Adjust the layout for better spacing
plt.show()
