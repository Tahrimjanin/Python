import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random


data = random.normal(loc=50, scale=10, size=1000)  

# 1. Histogram with KDE curve
sns.displot(data, kde=True)
plt.title("Histogram with KDE Curve")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2. KDE only 
sns.displot(data, kind="kde")
plt.title("Only KDE Curve")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

# 3. Histogram only 
sns.displot(data, kde=False)
plt.title("Only Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
