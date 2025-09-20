# Python script to plot deflection of a
# simply-supported beam under point load
# This plot is for half of the beam
import numpy as np
import matplotlib.pyplot as plt
# Beam parameters
L = 12000  # length in mm
I = 5 * (10**9) #moment of inertia(mm^4)
E = 200000 #modulus of elasticity(N/mm^2)
F = 500 * 1000  # force (N)
# CalculatING deflection, delta (mm)
x =np.arange(0,6001,200,dtype=np.int64)
delta =(F*x*((3*(L**2))-(4*(x**2))))/(48*E*I)
# Plotting
plt.plot(x, delta, '*k', markersize=15)
plt.xlabel('Distance (mm)', fontsize=30)
plt.ylabel('Deflection (mm)', fontsize=30)
plt.ylim([0, 20])  # limits of the y-axis
plt.gca().tick_params(axis='both',labelsize=30,
                      width=2.0)
plt.gca().spines['top'].set_linewidth(2.0)
plt.gca().spines['right'].set_linewidth(2.0)
plt.gca().spines['left'].set_linewidth(2.0)
plt.gca().spines['bottom'].set_linewidth(2.0)
plt.tight_layout()
plt.show()
# End of Python code.
