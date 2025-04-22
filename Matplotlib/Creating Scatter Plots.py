import matplotlib.pyplot as plt
import numpy as np

# Create random data with 100 points
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100) * 100  # Values for colormap
sizes = np.random.rand(100) * 1000  # Random sizes for each point

# Create scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='Accent') 

# Show colorbar to reflect the color values
plt.colorbar()

# Display the plot
plt.show()
