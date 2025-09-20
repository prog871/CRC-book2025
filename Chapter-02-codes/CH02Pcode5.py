# This code calculates the
# area of a triangle ABC
# by knowing the
# coordinates of A,B,and C
import numpy as np
# Give coordinates A,B,C
A = [20, 50]
B = [70, 5]
C = [75, 55]
# Construct the matrix
matrix = np.array([
    [A[0], A[1], 1],
    [B[0], B[1], 1],
    [C[0], C[1], 1]
])
# Calculate the determinant
deter = np.linalg.det(matrix)
# Calculate the area
Area = 0.5 * abs(deter)
# Display the result
print(f'Area={Area:.2f} m^2')
# End of Python script 
