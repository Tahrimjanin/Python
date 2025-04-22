import matplotlib.pyplot as plt
import numpy as np

# Bar chart example
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# Create a bar chart
plt.bar(x, y, color="hotpink")
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Horizontal bar chart example
plt.barh(x, y, color="skyblue")
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

# Histogram example
x = np.random.normal(170, 10, 250)  # Normal distribution with mean 170 and stddev 10

# Create a histogram
plt.hist(x, bins=15, color='green', edgecolor='black')
plt.title("Height Distribution Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()
