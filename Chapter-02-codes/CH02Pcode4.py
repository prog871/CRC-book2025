# This code solves the forces  
# of a triangular truss 
# using a system of three 
# linear equations
import numpy as np
# Define coefficient matrix A
A = np.array([[1/2, -1/2, 0],
  [-np.sqrt(3)/2,-np.sqrt(3)/2,0],
   [-1/2, 0, -1]])
# Define constants vector b
b = np.array([0, 10, 0])
# Solve for F_AC,F_AB,F_BC
x = np.linalg.solve(A, b)
# Display the solution
print("Solution:")
print(f"F_AC = {x[0]}")
print(f"F_AB = {x[1]}")
print(f"F_BC = {x[2]}")
