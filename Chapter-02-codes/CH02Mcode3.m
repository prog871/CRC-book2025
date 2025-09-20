% This code solves the reactions  
% of a simply-supported beam 
% using a system of two linear
% equations 
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Define the coefficient matrix A 
A = [1, 1; 0, 20];
% Dfine the right-hand side vector b
b = [10; 70];
% Solve the system Ax = b
x = A \ b;
% Display the results
R_A = x(1);
R_B = x(2);
% prinr the results
fprintf('R_A is %.2f kN.\n', R_A);
fprintf('R_B is %.2f kN.\n', R_B);
% end of M - file
