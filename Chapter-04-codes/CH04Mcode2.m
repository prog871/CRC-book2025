% Define symbolic variables
syms x y
%
% Define the function T(x,y)
T = x*exp(y) + y*sin(x);
%
% Compute partial derivatives
dTdx = diff(T, x);  % Partial derivative w.r.t. x
dTdy = diff(T, y);  % Partial derivative w.r.t. y
%
% Evaluate partial derivative w.r.t. x at (2,1)
val_dTdx_2_1 = subs(dTdx, [x, y], [2, 1]);
%
% Evaluate partial derivative w.r.t. y at (1,2)
val_dTdy_1_2 = subs(dTdy, [x, y], [1, 2]);
%
% Convert to double (numerical) for display
val_dTdx_2_1_num = double(val_dTdx_2_1);
val_dTdy_1_2_num = double(val_dTdy_1_2);
%
% Display results
disp(['dT/dx at (2,1) = ', num2str(val_dTdx_2_1_num)]);
disp(['dT/dy at (1,2) = ', num2str(val_dTdy_1_2_num)]);