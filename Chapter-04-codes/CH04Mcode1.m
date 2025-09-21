% Define symbolic variables
syms x y
%
% Define the temperature function T(x,y)
T = 18 - (3/2)*x^2 - y^2;
%
% Compute partial derivatives
dTdx = diff(T, x);
dTdy = diff(T, y);
%
% Evaluate partial derivative w.r.t. x at (1,0)
val_dTdx_1_0 = subs(dTdx, [x, y], [1, 0]);
%
% Evaluate partial derivative w.r.t. y at (0,3)
val_dTdy_0_3 = subs(dTdy, [x, y], [0, 3]);
%
% Display results
disp(['dT/dx at (1,0) = ', char(val_dTdx_1_0)]);
disp(['dT/dy at (0,3) = ', char(val_dTdy_0_3)]);