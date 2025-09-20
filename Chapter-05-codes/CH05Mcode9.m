%This code omputes the flow rate
% (Q) of an irregular river 
%using numerical integration.
clc; clear; close all;
% Input data
x=[0,2,4,6,8,10]; % x (m)
y=[0.5,0.7,1.2,1.5,1.1,0.8];%Depths(m)
v = 2; % Flow velocity (m/s)
% Calculate cross-section area (A) 
% using the trapezoidal rule
A = trapz(x, y);
% Calculate the flow rate
Q = v * A;
% Display results
fprintf('A = %.2f m^2\n',A);
fprintf('Q = %.2f m^3/s\n', Q);
% End of M - file
