%This code, named 'CH01Mcode2.m' 
% calculates stress inside a 
%column and determines if it is safe
clc ; % clear screen
clear ;%clear ariables from the memory
A = 2250000; % cross section area (mm^2)
F = 42000*1000; % force in N
allow_str=30;%allowabale stress(MPa=N/mm^2) 
% calculations
str= F/A; % calculate stress in MPa
display(str);
% Check if stress exceeds allowable limit
if str > allow_str
disp('str>allowabale stress;column fails');
else
disp('str<allowabale stress;column is safe');
end
% end of M - file
