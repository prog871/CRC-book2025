# This Python script, named 'CH01Pcode4.py', 
# calculates the deflection of a 
# simply-supported beam under point load
import numpy as np # importing module 'numpy'
L = 5000  # length in mm
I = 2.13 * (10**9)  # moment of inertia (mm^4)
E = 35000  # modulus of elasticity (N/mm^2)
F = np.array([50,60,70,80,90])*1000  #force(N)
# Calculations
delta = F * (L**3) / (48 * E * I)  #deflection(mm)
# Printing the results
print("Deflection (mm):", delta)
# End of Python script
