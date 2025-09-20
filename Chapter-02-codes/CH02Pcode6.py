# This code olves a system
# of two linear equations 
# using matrix inversion.
# 2x1 + 3x2 = 8
# x1 - 4x2 = -2
import numpy as np
# Define coefficient matrix A
A = np.array([[2, 3], [1, -4]])
# Define the constant matrix B
B = np.array([8, -2])
# Compute the inverse of A
A_inv = np.linalg.inv(A)
# Calculate solution vector x
x = np.dot(A_inv, B)
# Extract values of x1 and x2
x1 = x[0]
x2 = x[1]
# Display values of x1 and x2
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")
# end of Python code.
