%This code fits a least-square
%fitted line to fit data points. 
%using 'polyfit' function
clc; clear; close all;
set(0,'defaultaxesfontsize',28);
% Data points
x=[1, 2, 3, 4, 5, 6, 7]';
y=[2.1,4.5,6.3,8.0,10.1,12.2,14.5]';
% Fit a linear model
f=fit(x,y,'poly1'); % Linear fit
% Extract coefficients
m = f.p1; % Slope
a = f.p2; % Intercept
y2=m.*x+a; % y2 is from fitted line
figure;
plot(x,y,'o','MarkerSize',10);
hold on; % Retain current plot
plot(x,y2,'LineWidth',2);%Plot line 
xlabel('x'); ylabel('y');
xlim([0 7.5]); ylim([0 15]);
grid on;set(gca,'linewidth',1.5);
fprintf('Slope (m): %.3f\n',m);
fprintf('Intercept(a): %.3f\n',a);
% end of M - file
