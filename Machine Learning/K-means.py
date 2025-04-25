import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#  data points
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x, y)
plt.title('Original Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#  data for clustering
data = list(zip(x, y))

inertias = []
for i in range(1, 11): 
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method to Find Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.title('K-means Clustering Result (K=2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
