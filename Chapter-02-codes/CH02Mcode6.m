% This code olves a system
% of two linear equations 
% using matrix inversion.
% 2x1 + 3x2 = 8
% x1 - 4x2 = -2
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Define coefficient matrix A
A = [2, 3; 1, -4];
% Define constant matrix B
B = [8; -2];
% Compute the inverse of A
A_inv = inv(A);
% Calculate solution x
x = A_inv * B;
% Display the values of x1 and x2
x1 = x(1);
x2 = x(2);
fprintf('x1 = %.2f\n', x1);
fprintf('x2 = %.2f\n', x2);
% end of M - file
