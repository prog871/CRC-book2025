%this M-file , CH01Mcode7.m, 
%This code makes a bar chart of 
%materials used for beach nourishment
clc ; % clear screen
clear ; %clear  memory
set(0,'defaultaxesfontsize',30);%font
% Define materials and their volumes
mat={'Sand','Gravel','Shells','Silt', ...
    'Rock', 'Clay', 'Geotextiles'};
vol=[70,20,35,74,62,25,66];%Volumes(m^3)
% Create a bar chart
figure; % Open a new figure
bar(vol,'FaceColor','b'); % blue color
xlabel('Materials');ylabel('Volume (m^3)');
set(gca,'XTickLabel',mat);%x-axis labels
grid on;%Add grid for better readability
ylim([0 90]); % limit of y axis
set(gca,'linewidth',2.0);
% end of M - file
