%This M-file, named CH01Mcode3.m, 
%calculates deflection of a 
%simply-supported beam 
% under point load
clc ; % clear screen
clear; % clear memory
L = 5000; % length in mm
I=2.13*(10^9);%moment of inertia (mm^4)
E=35000;%modulus of elasticity (N/mm^2)
F = [50,60,70,80,90].*1000;% force (N) 
% calculating 'delta': deflection(mm) 
for i=1:5
delta(i)= F(i).*(L^3)./(48*E*I);
end
% printing the reslts 
display (delta, 'Deflection (mm)')
% end of M-file
