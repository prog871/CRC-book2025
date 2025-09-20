#This code gives mean 
#and %standard deviation for
#12 records and plots them
import numpy as np
import matplotlib.pyplot as plt
#Data:Compressive Strength(MPa)
A=np.array([32.1,33.4,31.8,32.9,34.2, 
33.0,31.5,32.7,33.8,32.3,34,31.9])
mean_A = np.mean(A)
std_A = np.std(A, ddof=0)  
plt.figure(figsize=(7, 8))
plt.plot(range(1, 13), A, 'ko',\
markersize=10, linewidth=2)
plt.axhline(mean_A, linestyle='--',\
color='b', linewidth=2.5)
plt.axhline(mean_A+std_A,linestyle='--',\
color='k', linewidth=2)
plt.axhline(mean_A-std_A,linestyle='--',\
color='k', linewidth=2)
plt.ylim([30, 36])
plt.xlim([0, 13])
plt.grid(True, linewidth=1.5)
print(f'Mean = {mean_A:.2f} MPa')
print(f'Std Deviation = {std_A:.2f} MPa')
plt.show()
# End of Python script
