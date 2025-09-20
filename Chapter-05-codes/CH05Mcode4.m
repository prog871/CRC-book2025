%This code computes tension (T)
%at the lowest point of cable 
%of a suspension bridge. 
% using 'fzero' function
clc; clear; close all;
% Define the function f(T)
f=@(T)(30375/(8*T))+(T/176711.11)-6;
%Provide an initial guess for T
ini_T=400; %Adjust if necessary
% Solve for T using 'fzero'
[T_sol,fval,exitflag]=fzero(f,ini_T);
% Display the results
if exitflag == 1
 fprintf('T = %.4f kN\n', T_sol);
 fprintf('f(T) = %.4f\n',fval);
else
 fprintf('fzero did not converge.\n');
end
% end of M - file
