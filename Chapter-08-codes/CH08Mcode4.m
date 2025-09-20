%This code plots the CDF
%for normal distribution
clc; clear; close all;
set(0,'defaultaxesfontsize',27)
mu=30;sigma=3; %mean & St. dev.(MPa)
x=25;%Strength value to check (MPa)
z = (x - mu) / sigma; %z-score
probab= normcdf(z);% probability
% Display the probability
fprintf(['The probability that ' ...
'compressive strength is less' ...
'than 25 MPa = %.4f\n'],probab);
subplot('position',[0.07 .1 .37 .7]);
fplot(@(x) normpdf(x, mu, sigma), ...
[mu-4*sigma,mu+4*sigma],'k','LineWidth',2);
hold on; grid on;
% Shade area to the left of x = 25
x_fill=linspace(mu - 4*sigma, x,100); 
y_fill = normpdf(x_fill, mu, sigma); 
fill([x_fill, x], [y_fill, 0], 'r', ...
'FaceAlpha', 0.3, 'EdgeColor', 'none'); 
% Add a vertical line at x = 25
line([x x],[0 10],'Color','k', ...
'LineStyle','--','linewidth',2);
set(gca,'linewidth',2); ylim([0 0.14])
%%%%%%%%%%%%%%%%%%%%%%%%
% Add CDF plot to the right
subplot('position',[.55 .1 .37 .7]); 
fplot(@(x) normcdf((x - mu)/sigma), ...
[mu-4*sigma,mu+4*sigma],'k','LineWidth',2);
hold on; grid on;
line([x x], [0 probab],'Color','k', ...
'LineStyle', '--', 'LineWidth', 2.0);
line([mu-4*sigma x], [probab probab], ...
'Color','k','LineStyle','--','LineWidth',2);
set(gca, 'linewidth', 2); ylim([0 1.05]);
% end of M - file
