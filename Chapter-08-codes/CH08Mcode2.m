%This code mean wave height 
%and standard deviation for
%heights of 30 storm waves 
clc; clear; close all;
%Wave height data (in meters)
wave_heights=[1.2,1.5,2.0,1.8,... 
1.7,2.2,2.5,2.8,1.9,1.6, ...
2.4,2.6,3.0,2.7,2.1,1.4,2.3,...
2.0,1.3,2.9,1.1,3.1,1.9, 2.2,...
2.7, 2.4,1.8,2.5,1.6, 2.3];
% Compute mean wave height
mean_height=mean(wave_heights);
% Compute standard deviation
std_dev = std(wave_heights,1); 
% Display results
fprintf('Mean height: %.2f m\n',...
mean_height);
fprintf('Std Deviation: %.2f m\n',...
std_dev);
% end of M - file
