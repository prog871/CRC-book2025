%This code gives mean 
%and %standard deviation for
%12 records and plots them
clc; clear; close all;
set(0,'defaultaxesfontsize',27)
%Data:Compressive Strength(MPa)
A = [32.1, 33.4,31.8, 32.9,34.2,...
33.0,31.5,32.7,33.8,32.3,34.0,31.9];
mean_A = mean(A);
std_A = std(A, 1);
% Plot the values as markers
subplot('position',[.2 .2 .5 .7]);
plot(1:12,A,'ko','MarkerSize',16,...
    'linewidth',2); 
hold on;
yline(mean_A, '--b','LineWidth',2.5);
% Plot (Mean ± Sigma)
yline(mean_A+std_A,'--k','LineWidth',2);
yline(mean_A-std_A,'--k','LineWidth',2);
ylim([30 36]); xlim([0 13]);
fprintf('Mean = %.2f MPa\n',mean_A);
fprintf('Std Deviation= %.2f MPa\n',std_A);
grid on;set(gca,'linewidth',1.5)
% end of M - file
