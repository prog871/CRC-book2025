#This code estimates the rate of 
#change of velocity (=acceleration)
#at x=40m using central difference
import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,10,20,30,40,50,60]) #(m)
v=np.array([1.5,1.8,2.0,2.4,2.8,3.1,3.5]) #(m/s)
#Acceleration using central difference
delta_x = 10  # Spacing (m)
v_for = 3.1  # v(x+delta_x) at x=50m
v_back = 2.4  # v(x-delta_x) at x=30m
acc = (v_for - v_back) / (2 * delta_x)
#Plot velocity vs. location
plt.figure(figsize=(8, 6))
plt.plot(x,v,'o-',linewidth=2,markersize=12)
plt.xlim(0, 63)
plt.ylim(1, 3.7)
plt.grid(True,linestyle='--',linewidth=1)
plt.xlabel('Location (m)',fontsize=14)
plt.ylabel('Velocity (m/s)', fontsize=14)
print(f'Calculated acceleration at \
x = 40 m: {acc:.4f} m/s^2')
plt.tight_layout(); plt.show()
#End of Python script
