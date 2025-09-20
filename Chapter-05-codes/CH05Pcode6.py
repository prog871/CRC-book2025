#This code fits a nonlinear least
#square curve to fit data points 
#using 'scipy.optimize.curve_fit'
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#Input data: head (H), discharge (Q)
H=np.array([.5,1,1.5,2,2.5,3]) #meters
Q=np.array([15,50,100,180,280,400]) #m^3/s
# Define the model function: Q=C*H^n
def modelF(H, C, n):
    return C * H**n
# Initial guess for C and n
ini_guess = [1, 1]
# Fit nonlinear model using curve_fit
par, _ =curve_fit(modelF,H,Q,p0=ini_guess)
# Extract fitted parameters
C, n = par
print(f"Results: C= {C:.4f}, n= {n:.4f}")
# Predictions using fitted model
H_pred=np.linspace(min(H),max(H),100)
Q_pred = modelF(H_pred, C, n)
# Plot original data & fitted curve
plt.figure(figsize=(8, 6))
plt.plot(H,Q,'ro', markersize=8,\
   label='Measured Data')
plt.plot(H_pred, Q_pred, 'b-', \
   linewidth=2,label='Fitted Curve')
plt.grid(True, linewidth=0.5)
plt.xlim([0,3.2]); plt.ylim([0,410])
plt.xlabel('Head, H (m)')
plt.ylabel('Discharge, Q (m³/s)')
plt.legend(loc='lower right')
plt.tight_layout(); plt.show()
# End of Python script
