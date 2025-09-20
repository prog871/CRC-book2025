#This Python code calculates
#deflection and rotation of
#the free end of a cantilever 
#beam using marix inversion
import numpy as np
# Given values
L = 4000  #Length of beam (mm)
E = 30000 #Young Modulus(N/mm^2)
I = 6.75e8 #2nd area moment(mm^4)
F = 6e3  # Force (N)
# Stiffness matrix calculation
k1 = (E * I)/L**3 #Stiffness
# Stiffness matrix
K = k1 * np.array([[12, -6 * L], 
          [-6 * L, 4 * L**2]])
# Force vector
F_vec = np.array([-F, 0])
# Matrix inversion
Delta = np.linalg.inv(K).dot(F_vec)
# Displacement (d),rotation(theta)
d = Delta[0]  # Displacement(mm)
theta = Delta[1]  #Rotation(radians)
# Display results
print(f'd = {d:.2f} mm')
print(f'theta = {theta:.4f} radians')
# end of Python code.
