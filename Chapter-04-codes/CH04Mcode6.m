function solve_ode1_symbolic
% ODE: y'(x) = x^2, y(0) = 0
% Using dsolve for a symbolic solution.
% 
syms x y(x)
%   
% Define the ODE symbolically
odeEqn = diff(y, x) == x^2;
%   
% Solve with the initial condition y(0) = 0
sol = dsolve(odeEqn, y(0) == 0);
%    
% Display the symbolic solution
disp('Symbolic solution for y(x):');
disp(sol);
end