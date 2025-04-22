import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])


plt.figure(figsize=(10, 6))

#1. Draw vertical bars with "hotpink" color and width of 0.1
plt.subplot(2, 2, 1) 
plt.bar(x, y, color="hotpink", width=0.1)
plt.title("Vertical Bars with hotpink color and width 0.1")

# Horizontal Bar Chart with height adjustment
# 2.Draw horizontal bars with "lightblue" color and height of 0.1
plt.subplot(2, 2, 2)  # Row 1, Column 2
plt.barh(x, y, color="lightblue", height=0.1)
plt.title("Horizontal Bars with lightblue color and height 0.1")

# Vertical Bar Chart with custom Hex color and width adjustment
#3. Draw vertical bars with custom hex color (#4CAF50) and width of 0.8
plt.subplot(2, 2, 3)  # Row 2, Column 1
plt.bar(x, y, color="#4CAF50", width=0.8)
plt.title("Vertical Bars with #4CAF50 and width 0.8")

# Horizontal Bar Chart with custom color names and height
# 4.Draw horizontal bars with "red" color and height of 0.2
plt.subplot(2, 2, 4)  # Row 2, Column 2
plt.barh(x, y, color="red", height=0.2)
plt.title("Horizontal Bars with red color and height 0.2")

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
