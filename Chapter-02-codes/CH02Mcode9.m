%This MATLAB code calculates
%the natural periods and modes
%of a two-story building.
clear; close all; clc
set(0,'defaultaxesfontsize',28);
m1=98/9810;%Mass, 1st story(kN.s^2/mm)
m2=79/9810;%Mass, 2nd story(kN.s^2/mm)
k1= 6;%Stiffness, 1st story(kN/mm)
k2= 6;%Stiffness, 2nd story(kN/mm)
%[M]:mass matrix,[K]:stiffness matrix
M = [m1, 0; 0, m2];
K = [k1 + k2, -k2; -k2, k2];
%Solve the eigenvalue problem
% [K - w^2 * M] * v = 0
% |K - w^2 * M|=0
%solve: 36−0.156ω^2+0.00008ω^4=0
% using function 'roots' in MATLAB
p=[0.00008  0  -0.156  0 36];
r=roots(p);
% find acceptable roots (eigenvalues)
k=1;
for i=1:4
    if r(i)>=0
        x(k)=r(i); k=k+1;
    end
end
% Sort 1st and 2nd mode
w1=x(1); w2=x(2);
if x(1)>x(2)
    w1=x(2); w2=x(1);
end
% Eigenvalues (angular frequencies)
fprintf('Eigenval 1 (w_1):%.2f\n',w1);
fprintf('Eigenval 2 (w_2):%.2f\n',w2);
% Calculate the natural periods
T1= 2*pi/w1; %1st natural period
T2= 2*pi/w2; %2nd natural period
% Display the natural periods
fprintf('Period 1 (T1):%.2f s\n',T1);
fprintf('Period 2 (T2):%.2f s\n',T2);
% 1st eigenvector (1st mode shape)
MK1=[k1 + k2-(m1*w1^2), -k2; ...
    -k2, k2-0.008*w1^2];
[eig_vec1,D]=eig(MK1);
v1= eig_vec1(:, 1); %1st eigenvector
v1=v1/v1(1);%Normalize to first element
% 2nd eigenvector (2nd mode shape)
MK2=[k1 + k2-(m1*w2^2), -k2; ...
    -k2, k2-0.008*w2^2];
[eig_vec2,D]=eig(MK2);
v2= eig_vec2(:, 2); %1st eigenvector
v2=v2/v2(1);%Normalize to first element
fprintf('Eigenvec 1:[%.2f,%.2f]\n',v1(1),v1(2));
fprintf('Eigenvec 2:[%.2f,%.2f]\n',v2(1),v2(2));
% end of M - file
