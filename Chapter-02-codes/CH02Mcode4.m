% This code solves the forces  
% of a triangular truss 
% using a system of three linear
% equations 
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Define the coefficient matrix A
A = [1/2, -1/2, 0;
     -sqrt(3)/2, -sqrt(3)/2, 0;
     -1/2, 0, -1];
% Define the constants vector b
b = [0; 10; 0];
% Solve for unknowns (F_AC,F_AB,F_BC)
x = A \ b;
% Display the solution
disp('Solution:');
disp(['F_AC = ',num2str(x(1))]);
disp(['F_AB = ',num2str(x(2))]);
disp(['F_BC = ',num2str(x(3))]);
% end of M - file
