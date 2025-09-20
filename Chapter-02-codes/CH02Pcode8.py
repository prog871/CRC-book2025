#This Python code calculates
#the eigenvalues & eigenvectors
#of a matrix A=[4, 1; 2, 3]
import numpy as np
#Given matrix A
A = np.array([[4, 1], [2, 3]])
#Use numpy.linalg.eig() for
#eigenvalues & eigenvectors
eig_val,eig_vec=np.linalg.eig(A)
#The diagonal of eig_val
#contains the eigenvalues
lam1=eig_val[0] #1st eigenvalue
lam2=eig_val[1] #2nd eigenvalue
#Display eigenvalues
print(f'Eigenvalue 1:{lam1:.2f}')
print(f'Eigenvalue 2:{lam2:.2f}')
#The eigenvectors are stored in
#the columns of eig_vec
v1=eig_vec[:, 0]  #1st eigenvector
v2=eig_vec[:, 1]  #2nd eigenvector
#Display eigenvectors (usually
#normalized by dividing by first element)
print(f'Eigenvec 1:[{v1[0]/v1[0]:.2f},',end='')
print(f'{v1[1]/v1[0]:.2f}]')
print(f'Eigenvec 2:[{v2[0]/v2[0]:.2f},',end='')
print(f'{v2[1]/v2[0]:.2f}]')
# end of Python code.
