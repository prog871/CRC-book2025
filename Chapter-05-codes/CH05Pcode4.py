#This code computes tension (T)
#at the lowest point of cable
#using 'fsolve' function
import numpy as np
from scipy.optimize import fsolve
# Define the function f(T)
def f(T):
 return (30375/(8*T))+(T/176711.11)-6
# Provide initial guess for T
ini_T=400  #Adjust if needed
# Solve for T using 'fsolve'
T_sol = fsolve(f, ini_T)
# Display the results
print(f'T = {T_sol[0]:.4f} kN')
print(f'f(T) = {f(T_sol[0]):.4f}')
# End of Python script
