%Function to calculate volume and weight
function [V_e, Wgt]=CH01Mcode5(L,W,H,gamma)
clc; close all; % clear memory 
%This function calculates volume and weight
%given length(L),width(W),height(H),
%and density(gamma)
%dimensions in meters and gamma in kg/m^3
%Calculate volume (V_e =L*W* H)
V_e = L * W * H; % volume in m^3
% Calculate weight (Wgt = V_e * gamma)
Wgt = V_e * gamma; % weight in kg
end
% end of M - file
