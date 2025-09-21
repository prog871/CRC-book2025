% Define the symbolic variable
syms t
% Define the function f(t)
f = t^2 + t;
% Calculate the derivative of f(t)
f_derivative = diff(f, t);
% Simplify the derivative (if applicable)
f_derivative_simplified = simplify(f_derivative);
% Display the results
fprintf('The derivative of f(t) is %s\n', char(f_derivative));