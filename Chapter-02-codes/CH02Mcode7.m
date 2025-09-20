%This MATLAB code calculates
%deflection and rotation of
%the free end of a cantilever 
%beam using marix inversion 
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Given values
L =4000;%Length of beam(mm)
E =30000;%Young Modulus(N/mm^2)
I =6.75e8;%2nd area moment (mm^4)
F =6e3; % Force  (N)
% Stiffness matrix calculation
k1 = (E * I) / L^3;% Stiffness
% Stiffness matrix
K = k1 * [12,-6*L;-6*L,4*L^2];
% Force vector
F_vec = [-F; 0];
% Matrix inversion
Delta = inv(K) * F_vec;
% Displacement(d), rotation(theta)
d = Delta(1); %displacement(mm)
theta = Delta(2);%rotation(radians)
% Display results
fprintf('d = %.2f mm\n', d);
fprintf('theta = %.4f radians\n',theta);
% end of M - file
