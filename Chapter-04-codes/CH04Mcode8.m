function solve_ode2_symbolic
% ODE: y'(x) + y(x) = x^2, y(0) = 1
% Symbolic solution with dsolve.
syms x y(x)
odeEqn = diff(y, x) + y == x^2;
sol = dsolve(odeEqn, y(0) == 1);
disp('Symbolic solution for y(x):');
disp(sol);
end