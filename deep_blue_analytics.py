# Only import what's actually used
import numpy as np

# Use numpy array for better performance with numerical operations
x = np.array([1, 2, 3, 4])

# Calculate squares more efficiently using numpy vectorization
squares = x**2

# Eliminate loops entirely - use numpy's vectorized string operations
# This is faster than iterating and calling print() multiple times
print('\n'.join(map(str, squares)))
print('\n'.join(map(str, x)))
