from numpy import random

print("RANDOM INTEGER ")
# Random integer from 0 to 100
x = random.randint(100)
print("Random Integer 0-100:", x)

print("\nRANDOM FLOAT ")
# Random float from 0 to 1
x = random.rand()
print("Random Float 0-1:", x)

print("\nRANDOM ARRAY OF INTEGERS")
# 1-D array with 5 random integers
x = random.randint(100, size=(5))
print("1D Array (5 random integers 0-100):", x)

# 2-D array (3 rows, 5 columns) of random integers
x = random.randint(100, size=(3, 5))
print("2D Array (3x5 random integers 0-100):\n", x)

print("\nRANDOM ARRAY OF FLOATS")
# 1-D array with 5 random floats
x = random.rand(5)
print("1D Array (5 random floats 0-1):", x)

# 2-D array (3 rows, 5 columns) of random floats
x = random.rand(3, 5)
print("2D Array (3x5 random floats 0-1):\n", x)

print("\nRANDOM CHOICE FROM ARRAY")
x = random.choice([3, 5, 7, 9])
print("Random Choice (single value from [3,5,7,9]):", x)

# Randomly pick values to create a 2D array
x = random.choice([3, 5, 7, 9], size=(3, 5))
print("Random Choice (3x5 array from [3,5,7,9]):\n", x)

print("\nRANDOM CHOICE WITH DEFINED PROBABILITIES")
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print("Random Choice (100 values with probabilities p=[0.1, 0.3, 0.6, 0.0]):\n", x)

# 2-D array with probabilities
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print("Random Choice (3x5 array with probabilities p=[0.1, 0.3, 0.6, 0.0]):\n", x)
