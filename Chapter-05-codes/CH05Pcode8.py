#This code estimates integral
#of f(x)=x^2 at interval [0,8]
import numpy as np
# Define interval and step size
x = np.arange(0, 8.05, 0.05)  
y = x**2  #Function values at points x
# Compute the integral 
area = np.trapz(y, x)
# Display the result
print(f"Integral = {area}")
#End of Python script
