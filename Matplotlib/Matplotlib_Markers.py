import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.figure(figsize=(12, 8)) #12 inches wide and 8 inches tall for better visibility

# 1. Basic Circle Marker
plt.subplot(2, 3, 1)
plt.plot(ypoints, marker='o') #if wanna make another maker change the marker like ('*','v', 's', '^', 'x', etc.)
plt.title("Circle Marker (o)")

# 2. Star Marker with fmt shortcut and red dotted line
plt.subplot(2, 3, 2)
plt.plot(ypoints, '*:r') # r= color representator (r=red, g=green, b=blue, etc.), * = star marker, : = dotted line
plt.title("Star Marker + Dotted Line")

# 3. Circle marker with big size
plt.subplot(2, 3, 3)
plt.plot(ypoints, marker='o', ms=20) # ms = marker size
plt.title("Big Marker (size = 20)")

# 4. Edge color red
plt.subplot(2, 3, 4)
plt.plot(ypoints, marker='o', ms=15, mec='r')# mec = marker edge color
plt.title("Edge Color Red (mec='r')") 

# 5. Face color red
plt.subplot(2, 3, 5)
plt.plot(ypoints, marker='o', ms=15, mfc='r') #mfc = marker face color
plt.title("Face Color Red (mfc='r')")

# 6. Full marker color with hex code
plt.subplot(2, 3, 6)
plt.plot(ypoints, marker='o', ms=15, mec='#4CAF50', mfc='#4CAF50')#the edge and face color of the markers to a custom hexadecimal green color (#4CAF50).
plt.title("Hex Color (#4CAF50)")

plt.tight_layout()
plt.show()
