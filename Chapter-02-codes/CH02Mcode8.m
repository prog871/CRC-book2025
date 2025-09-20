%This MATLAB code calculates
%the eigenvalues and eigenvectors
%of a matrix A=[4, 1; 2, 3]
clear; close all; clc
set(0,'defaultaxesfontsize',28);
% Given matrix A
A = [4, 1; 2, 3];
% Use the eig() for 
[eig_vec, eig_val] = eig(A);
%The diagonal of eigenvalue matrix
%contains the eigenvalues
lam1 = eig_val(1,1);%1st eigenvalue
lam2 = eig_val(2,2);%2nd eigenvalue
% Display eigenvalues
fprintf('Eigenvalue 1: %.2f\n',lam1);
fprintf('Eigenvalue 2: %.2f\n',lam2);
% The eigenvectors are stored in the
% columns of the eigenvectors matrix
v1= eig_vec(:,1);%1st eigenvector
v2= eig_vec(:,2);%2nd eigenvector
% Display eigenvectors- note: usually
% the first element of eigenvectors
% is 1; that is why below the elements
% are divided to the first element 
fprintf(['Eigenvector 1: ' ...
 '[%.2f, %.2f]\n'], v1(1)/v1(1), ...
    v1(2)/v1(1));
fprintf(['Eigenvector 2: ' ...
 '[%.2f, %.2f]\n'], v2(1)/v2(1), ...
    v2(2)/v2(1));
% end of M - file
