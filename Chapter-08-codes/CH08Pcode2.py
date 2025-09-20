#This code mean wave height 
#and standard deviation for
#heights of 30 storm waves 
import numpy as np
# Wave height data (in meters)
wave_heights=[1.2,1.5,2.0,1.8, 
 1.7,2.2,2.5,2.8,1.9,1.6, 
 2.4,2.6,3.0,2.7,2.1,1.4, 2.3, 
 2.0,1.3,2.9,1.1,3.1,1.9, 2.2, 
 2.7,2.4,1.8,2.5,1.6,2.3]
# Compute mean wave height
mean_height=np.mean(wave_heights)
# Compute standard deviation
# ddof=0 population std deviation
std_dev=np.std(wave_heights, ddof=0)
# Display results
print(f'Mean height: {mean_height:.2f} m')
print(f'Std Deviation: {std_dev:.2f} m')
# End of Python script
