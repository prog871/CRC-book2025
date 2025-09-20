% This code calculates the total 
% construction cost for each 
% section of a 3 section road
clc ; % clear screen
clear ; % clear ariables from the memory
%
M=[10,15,5;8,20,6;12,18,7];
% Cost per ton (£)
C = [50; 30; 100];
% Total cost calculation (C_T)
C_T = M * C;
% Display results
disp('Total cost for each section (in £):');
disp(C_T);
%
% end of M - file
