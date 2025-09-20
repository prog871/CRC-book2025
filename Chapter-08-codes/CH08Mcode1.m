% This code plots a histogram
% for heights of 30 storm waves 
clc; clear; close all;
set(0,'defaultaxesfontsize',28);
clc; clear; close all;
set(0,'defaultaxesfontsize',28);
% Wave height data
wave_heights = [1.2,1.5,2.0,1.8,... 
1.7,2.2,2.5,2.8,1.9,1.6, ...
2.4,2.6,3.0,2.7,2.1,1.4,2.3,...
2.0,1.3,2.9,1.1,3.1,1.9, 2.2,...
2.7, 2.4,1.8,2.5,1.6, 2.3];
% Define class intervals
edges = [1.0,1.5,2.0,2.5,3.0,3.5];
%Plot histogram using specified bins
subplot('position',[0.2 0.2 0.5 0.7]);
histogram(wave_heights,'BinEdges',edges,...
'FaceColor','b','EdgeColor','k', ...
'LineWidth',1.5);
set(gca,'linewidth',1.5); grid on;
% end of M - file
