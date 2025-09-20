%this M-file , CH01Mcode6.m, 
%plots variations of deflection for 
%simply-supported beam under point load
%this plot is for half of the beam
clc ; % clear screen
clear ; % clear memory
set(0,'defaultaxesfontsize',30);%fontsize
L=12000; % length in mm
I=5*(10^9);%moment of inertia (mm^4)
E=200000;%modulus of elasticity(N/mm^2)
F=500.*1000; % force (N) 
% calculations of deflection(mm)
x=0:200:6000;
delta= F.*x.*(3*L.^2 -4*x.^2)./(48*E*I);
% plotting 
plot(x,delta,'*k','markersize',15);
xlabel('Distance (mm)');
ylabel('Deflection (mm)');
ylim([0 20]);% limits of the y axis
set(gca,'linewidth',2.0);
% end of M - file
