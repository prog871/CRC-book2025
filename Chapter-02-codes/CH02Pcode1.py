# This code calculates the total 
# construction cost for each 
# section of a 3-section road
import numpy as np  #Import NumPy
# Define matrix of quantities (M) in tons
M = np.array([
    [10, 15, 5],
    [8, 20, 6],
    [12, 18, 7]
])
# Define cost per ton (GBP) as a vector
C = np.array([50, 30, 100])
# Calculate total cost for each section (C_T)
C_T = np.dot(M, C)
# Display results
print("Total cost for each section (GBP):")
print(C_T)
# End of Python script