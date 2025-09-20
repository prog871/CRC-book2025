#This code omputes the flow rate
# (Q) of an irregular river 
#using numerical integration.
import numpy as np
# Input data
x=np.array([0,2,4,6,8,10])  # x(m)
y=np.array([0.5,0.7,1.2,1.5,1.1,0.8])
v = 2  # Flow velocity (m/s)
# Calculate cross-sectional area (A)
# using the trapezoidal rule
A = np.trapz(y, x)
# Calculate the flow rate
Q = v * A
# Display results
print(f"A = {A:.2f} m^2")
print(f"Q = {Q:.2f} m^3/s")
#End of Python script
