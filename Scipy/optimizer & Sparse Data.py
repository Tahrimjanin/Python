import numpy as np
from math import cos
from scipy.optimize import root, minimize
from scipy.sparse import csr_matrix

#SciPy Optimizer

# root of the equation x + cos(x)
def root_eqn(x):
    return x + cos(x)

myroot = root(root_eqn, 0)
print("Root of the equation x + cos(x):")
print(myroot.x) 
print("\nFull root object:")
print(myroot)  

#  Minimizthe function x^2 + x + 2
def min_eqn(x):
    return x**2 + x + 2

mymin = minimize(min_eqn, 0, method='BFGS')
print("\nMinimization of x^2 + x + 2:")
print(mymin)

#SciPy Sparse Data 

# CSR matrix-1D array
array1 = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
csr1 = csr_matrix(array1)
print("\nCSR Matrix from 1D array:")
print(csr1)

#CSR matrix-2D array
array2 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
csr2 = csr_matrix(array2)

print("\nStored data in CSR matrix:")
print(csr2.data)

print("\nNumber of non-zero elements:")
print(csr2.count_nonzero())

csr2.eliminate_zeros()
print("\nMatrix after eliminating zeros:")
print(csr2)

csr2.sum_duplicates()
print("\nMatrix after summing duplicates:")
print(csr2)

# Convert CSR to CSC
csc_matrix = csr2.tocsc()
print("\nConverted CSC Matrix:")
print(csc_matrix)
