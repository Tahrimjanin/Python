import matplotlib.pyplot as plt
import numpy as np

# 1. Simple line from (1, 3) to (8, 10)
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.figure(figsize=(10, 6))  # full graph size
plt.subplot(2, 2, 1)         # 2 rows, 2 columns, 1st plot
plt.plot(xpoints, ypoints)
plt.title("Simple Line Plot")

#  2. Plotting only markers
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.subplot(2, 2, 2)        # 2 rows, 2 columns, 2nd plot
plt.plot(xpoints, ypoints, 'o')  
plt.title("Only Markers")

# 3. Multiple points 
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3nd plot
plt.plot(xpoints, ypoints)
plt.title("Multiple Points Line")

# 4. Default X-points (0, 1, 2, ...)
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.subplot(2, 2, 4)  # 2 rows, 2 columns, 4th plot
plt.plot(ypoints)  # x-point  0,1,2,3...
plt.title("Default X-Points")

# Show all plots
plt.tight_layout()
plt.show()
