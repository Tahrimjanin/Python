import numpy as np
import matplotlib.pyplot as plt


fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# 1. Scatter plot using car age vs speed
x1 = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y1 = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

axs[0].scatter(x1, y1, color='blue')
axs[0].set_title("Car Age vs Speed")
axs[0].set_xlabel("Car Age")
axs[0].set_ylabel("Car Speed")

# 2. Scatter plot using random data from normal distribution
x2 = np.random.normal(5.0, 1.0, 1000)
y2 = np.random.normal(10.0, 2.0, 1000)

axs[1].scatter(x2, y2, color='green', alpha=0.5)
axs[1].set_title("Random Normal Distribution Scatter")
axs[1].set_xlabel("X ~ N(5.0, 1.0)")
axs[1].set_ylabel("Y ~ N(10.0, 2.0)")


plt.tight_layout()
plt.show()
