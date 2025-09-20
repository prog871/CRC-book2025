% This code plots the oscillatins 
% of the 2018 Palu tsunami 
% note that this codes needs
% an input file named 
% 'CH02-data-tsunami-Palu.txt'.
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Raed input data (tsunami time series)
data=load('CH02-data-tsunami-Palu.txt');
% plot time series
plot(data(:,1),data(:,2),'b','linewidth',1.5)
% add axis lables
xlabel('Time (min)'); ylabel('Sea level (cm)');
% limit of x-axis & y-axis
xlim([0 90]); ylim([-210 210]);
set(gca,'linewidth', 1.5);
% end of M - file
