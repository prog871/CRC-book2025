%This code estimates the rate of 
%change of velocity (=acceleration)
% at x=40m using central difference
clc; clear; close all;
set(0,'defaultaxesfontsize',28);
x=[0,10,20,30,40,50,60];%Location(m)
v=[1.5,1.8,2.0,2.4,2.8,3.1,3.5];%Velocity
%Acceleration using central difference 
delta_x=10; %Spacing (m)
v_for=3.1; %v(x+delta_x) at x=50m
v_back=2.4; %v(x-delta_x) at x=30m
acc=(v_for - v_back)/(2*delta_x);
% Plot velocity vs. location
subplot('position',[0.15 0.2 0.5 0.6]);
plot(x,v,'o-','LineWidth',2,'MarkerSize',12);
xlim([0 63]);ylim([1 3.7]);
set(gca,'linewidth',1.5); grid on; 
% Print calculated acceleration
fprintf(['Calculated acceleration at ' ...
    'x = 40 m: %.4f m/s^2\n'], acc);
% End of M - file
