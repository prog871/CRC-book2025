import numpy as np
import matplotlib.pyplot as plt
# Read input data (tsunami time series)
data=np.loadtxt('CH02-data-tsunami-Palu.txt')
# Plot time series
plt.plot(data[:,0],data[:,1],'b',linewidth=1.5)
# Add axis labels
plt.xlabel('Time (min)')
plt.ylabel('Sea level (cm)')
# Set limits for x-axis and y-axis
plt.xlim([0, 90])
plt.ylim([-210, 210])
# Set axis line width
plt.gca().tick_params(width=1.5)
# Show the plot
plt.show()
# End of Python code
