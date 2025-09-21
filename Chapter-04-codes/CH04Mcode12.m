function solve_ode2_symbolic
% ODE: y'' + 2y' + y = x^2,  y(0)=0, y'(0)=0
syms x y(x)
Dy = diff(y, x);
D2y = diff(y, x, 2);
odeEqn = D2y + 2*Dy + y == x^2;
% Initial conditions
conds = [y(0) == 0, Dy(0) == 0];
% Solve the ODE
sol = dsolve(odeEqn, conds);
disp('Symbolic solution for y(x):');
disp(sol);
end
