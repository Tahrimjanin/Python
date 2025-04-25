import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import (
    connected_components,
    dijkstra,
    floyd_warshall,
    bellman_ford,
    depth_first_order,
    breadth_first_order
)

# Adjacency Matrix 
arr1 = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

graph1 = csr_matrix(arr1)

print("Connected Components")
n_components, labels = connected_components(graph1)
print("Number of components:", n_components)
print("Labels:", labels)

print("\nDijkstra's Algorithm (from node 0)")
dist_matrix, predecessors = dijkstra(graph1, return_predecessors=True, indices=0)
print("Distances:", dist_matrix)
print("Predecessors:", predecessors)

print("\nFloyd-Warshall (All-Pairs Shortest Paths)")
fw_distances, fw_predecessors = floyd_warshall(graph1, return_predecessors=True)
print("Distances:\n", fw_distances)
print("Predecessors:\n", fw_predecessors)

#Negative Weight for Bellman-Ford
arr2 = np.array([
    [0, -1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

graph2 = csr_matrix(arr2)

print("\nBellman-Ford (from node 0, with negative weight) ")
bf_distances, bf_predecessors = bellman_ford(graph2, return_predecessors=True, indices=0)
print("Distances:", bf_distances)
print("Predecessors:", bf_predecessors)

# DFS and BFS 
arr3 = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])

graph3 = csr_matrix(arr3)

print("\n Depth First Order (from node 1)")
dfs_nodes, dfs_predecessors = depth_first_order(graph3, 1)
print("DFS Nodes:", dfs_nodes)
print("Predecessors:", dfs_predecessors)

print("\nBreadth First Order (from node 1) ")
bfs_nodes, bfs_predecessors = breadth_first_order(graph3, 1)
print("BFS Nodes:", bfs_nodes)
print("Predecessors:", bfs_predecessors)
