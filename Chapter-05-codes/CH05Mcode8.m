%This code estimates the integral
%of f(x)=x^2 at the interval [0,8]
clc; clear; close all;
x=0:0.05:8; % Interval [0, 8] divided 
% into 160 subintervals (Delta-x=0.05)
y=x.^2;  %Function values at points x
% Compute integral using 'trapz' 
area = trapz(x, y);
% Display the result
disp(['Integral = ', num2str(area)]);
% End of M - file
