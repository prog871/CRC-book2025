% This code calculates the   
% area of a triangle ABC
% by knowing the coordinates 
% of A, B and C 
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Give coordinates of A,B,C
A = [20, 50];
B = [70, 5];
C = [75, 55];
% Construct the matrix
matrix = [
    A(1), A(2), 1;
    B(1), B(2), 1;
    C(1), C(2), 1
];
% Calculate the determinant
determinant = det(matrix);
% Calculate the area
Area = 0.5*abs(determinant);
% Display the result
fprintf('Area = %.2f m^2\n',Area);
% end of M - file
