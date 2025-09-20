#This code solves the reactions
#of a simply-supported beam
#using a system of 2 linear equations
import numpy as np
# Define the coefficient matrix A
A = np.array([[1, 1], [0, 20]])
# Define right-hand side vector b
b = np.array([10, 70])
# Solve the system Ax = b
x = np.linalg.solve(A, b)
# Extract the results
R_A = x[0]
R_B = x[1]
# Print the results
print(f'R_A is {R_A:.2f} kN.')
print(f'R_B is {R_B:.2f} kN.')
# End of Python script
