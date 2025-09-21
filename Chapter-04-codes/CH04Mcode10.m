function solve_ode1_symbolic
% ODE: y''(x) = 6x, with y(0)=2, y'(0)=1.
syms x y(x)
%   
% Define the ODE:
odeEqn = diff(y, 2) == 6*x;
%   
% Define the derivative:
Dy = diff(y, x);
%  
% Initial conditions:
conds = [y(0) == 2, Dy(0) == 1];
%
% Solve the ODE with the initial conditions:
sol = dsolve(odeEqn, conds);  
disp('Symbolic solution for y(x):');
disp(sol);
end
