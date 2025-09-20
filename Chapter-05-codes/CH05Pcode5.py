#This code fits a linear least
#square line to fit data points. 
#using 'numpy.polyfit' function
import numpy as np
import matplotlib.pyplot as plt
# Data points
x=np.array([1,2,3,4,5,6,7])
y=np.array([2.1,4.5,6.3,8.0,10.1,12.2,14.5])
# Fit a linear model
coeff=np.polyfit(x,y,1) #Linear fit
m = coeff[0]  # Slope
a = coeff[1]  # Intercept
#Calculate fitted line values
y2=m*x+a  #y2 is from fitted line
# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x,y,'o',markersize=10)  
plt.plot(x,y2,linewidth=2)
plt.xlabel('x'); plt.ylabel('y')
plt.xlim([0,7.5]);plt.ylim([0,15])
plt.gca().tick_params(axis='both')
# Print results
print(f"Slope (m): {m:.3f}")
print(f"Intercept (a): {a:.3f}")
plt.show()
# End of Python script
