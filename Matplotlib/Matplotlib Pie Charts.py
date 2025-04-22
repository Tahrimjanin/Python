import matplotlib.pyplot as plt
import numpy as np

# Data
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]  # Explode Apples
mycolors = ["black", "hotpink", "blue", "#4CAF50"]  # Custom colors

# Create pie chart with all customizations
plt.pie(y, 
        labels=mylabels, 
        explode=myexplode, 
        colors=mycolors, 
        startangle=90, 
        shadow=True)

# Add legend with title
plt.legend(title="Four Fruits:")
plt.show()
