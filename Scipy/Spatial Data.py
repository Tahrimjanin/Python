import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, ConvexHull, KDTree
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming

# Triangulation 
points_triangulation = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])
simplices = Delaunay(points_triangulation).simplices

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.triplot(points_triangulation[:, 0], points_triangulation[:, 1], simplices)
plt.scatter(points_triangulation[:, 0], points_triangulation[:, 1], color='r')
plt.title("Delaunay Triangulation")

# Convex Hull 
points_hull = np.array([
    [2, 4], [3, 4], [3, 0], [2, 2],
    [4, 1], [1, 2], [5, 0], [3, 1],
    [1, 2], [0, 2]
])
hull = ConvexHull(points_hull)
hull_points = hull.simplices

plt.subplot(2, 2, 2)
plt.scatter(points_hull[:, 0], points_hull[:, 1])
for simplex in hull_points:
    plt.plot(points_hull[simplex, 0], points_hull[simplex, 1], 'k-')
plt.title("Convex Hull")

#  KDTree
points_kdtree = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points_kdtree)
res_kdtree = kdtree.query((1, 1))

print("KDTree Nearest Neigh:", res_kdtree)
#Distance Metrics 
p1 = (1, 0)
p2 = (10, 2)

euclid = euclidean(p1, p2)
city = cityblock(p1, p2)
cos = cosine(p1, p2)

print("Euclidean Distance:", euclid)
print("Cityblock Distance:", city)
print("Cosine Distance:", cos)

# Hamming Distance
p1_hamming = (True, False, True)
p2_hamming = (False, True, True)

ham = hamming(p1_hamming, p2_hamming)
print("Hamming Distance:", ham)

plt.subplot(2, 2, 3)
plt.axis('off')
plt.text(0, 0.5, f"KDTree:\nDistance: {res_kdtree[0]}\nIndex: {res_kdtree[1]}\n\n"
                 f"Euclidean: {euclid:.4f}\nCityblock: {city}\n"
                 f"Cosine: {cos:.4f}\nHamming: {ham:.4f}",
         fontsize=12, verticalalignment='center')

plt.tight_layout()
plt.show()
