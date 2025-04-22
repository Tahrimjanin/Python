import matplotlib.pyplot as plt
import numpy as np

# Data points
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.figure(figsize=(12, 8))  #Set the size of the figure

# 1. Solid line (default) with hotpink color and circle markers
plt.subplot(2, 3, 1)
plt.plot(y1, linestyle='solid', color='hotpink', marker='o', label='Solid Line')
plt.title("Solid Line + Hotpink")
plt.legend()

# 2. Dotted line with red color using short syntax
plt.subplot(2, 3, 2)
plt.plot(y1, ls=':', c='r', label='Dotted Red')
plt.title("Dotted Line (red)")
plt.legend()

# 3. Dashed line with green hex color and line width
plt.subplot(2, 3, 3)
plt.plot(y1, ls='--', c='#4CAF50', lw=3, label='Dashed Green')
plt.title("Dashed Line + Hex Color")
plt.legend()

# 4. Dash-dot line with blue color and star marker
plt.subplot(2, 3, 4)
plt.plot(y1, linestyle='-.', color='blue', marker='*', label='DashDot + *')
plt.title("Dash-dot Line + Star")
plt.legend()

# 5. Multiple lines in same plot
plt.subplot(2, 3, 5)
plt.plot(y1, label='Line 1', color='purple')
plt.plot(y2, label='Line 2', color='orange')
plt.title("Two Lines")
plt.legend()

# 6. Custom x and y values for two lines in one plot
plt.subplot(2, 3, 6)
plt.plot(x1, y1, 'g--o', label='x1-y1')  # green dashed line with circle marker
plt.plot(x1, y2, 'm-.s', label='x1-y2')  # magenta dash-dot line with square marker
plt.title("x-y Pairs for Two Lines")
plt.legend()

plt.tight_layout()
plt.show()
