#This code plots a histogram
#for heights of 30 storm waves
import numpy as np
import matplotlib.pyplot as plt
# Wave height data
wave_heights =[1.2,1.5,2.0,1.8, 
1.7, 2.2, 2.5, 2.8, 1.9, 1.6, 
2.4,2.6,3.0,2.7,2.1,1.4,2.3,
2.0,1.3, 2.9,1.1,3.1,1.9,2.2,
2.7, 2.4,1.8,2.5,1.6,2.3]
# Define class intervals
edges=[1.0,1.5,2.0,2.5,3.0,3.5]
# Create figure and axis
fig,ax=plt.subplots(figsize=(6,5))  
# Plot histogram
ax.hist(wave_heights,bins=edges,\
color='b',edgecolor='k',linewidth=1.5)
# Customize plot
ax.grid(True,linestyle='--',alpha=0.6)  
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
# Show plot
plt.show()
# End of Python script
