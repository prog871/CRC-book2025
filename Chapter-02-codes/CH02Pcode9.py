#This Python code calculates
#the natural periods and modes
#of a two-story building.
import numpy as np
# Mass and stiffness values
m1=98/ 9810  #Mass,1st story(kN.s^2/mm)
m2=79/ 9810  #Mass,2nd story(kN.s^2/mm)
k1=6 #Stiffness,1st story (kN/mm)
k2=6  #Stiffness,2nd story (kN/mm)
#Mass matrix[M], stiffness matrix[K]
M=np.array([[m1,0],[0,m2]])
K=np.array([[k1+k2,-k2],[-k2,k2]])
# Solve:36−0.156w^2+0.00008w^4=0
p = [0.00008, 0, -0.156, 0, 36]
r = np.roots(p)
# Find acceptable roots(eigenvalues)
x = [root for root in r 
     if np.isreal(root) and root >= 0]
x = sorted(np.real(x))  #Sort roots
w1, w2 = x[0], x[1]
# Eigenvalues (angular frequencies)
print(f"Eigenval 1 (w_1):{w1:.2f}")
print(f"Eigenval 2 (w_2):{w2:.2f}")
# Calculate natural periods
T1 = 2*np.pi/w1  #1st period
T2 = 2*np.pi/w2  #2nd period
print(f"Period 1 (T1):{T1:.2f}s")
print(f"Period 2 (T2):{T2:.2f}s")
# 1st eigenvector(1st mode shape)
MK1 = K - (w1**2) * M
eig_vals1,eig_vecs1=np.linalg.eig(MK1) 
idx1 = np.argmin(np.abs(eig_vals1))
v1=eig_vecs1[:,idx1]  #Select eigenvector
v1=v1/v1[0]  #Normalize to first element
# 2nd eigenvector (2nd mode shape)
MK2 = K - (w2**2) * M
eig_vals2, eig_vecs2 = np.linalg.eig(MK2)
idx2 = np.argmin(np.abs(eig_vals2))
v2=eig_vecs2[:,idx2]  #Select eigenvector
v2=v2/v2[0]  #Normalize to first element
print(f"Eigenvec 1:[{v1[0]:.2f},{v1[1]:.2f}]")
print(f"Eigenvec 2:[{v2[0]:.2f},{v2[1]:.2f}]")
# end of Python code.
