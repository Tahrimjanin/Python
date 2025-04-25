import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

# Dendrogram
linkage_data = linkage(data, method='ward', metric='euclidean')
plt.figure(figsize=(8, 4))
dendrogram(linkage_data)
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# Agglomerative Clustering
hierarchical_cluster = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

# Scatter Plot
plt.figure(figsize=(6, 6))
plt.scatter(x, y, c=labels, cmap='rainbow')
plt.title("Hierarchical Clustering Result")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
