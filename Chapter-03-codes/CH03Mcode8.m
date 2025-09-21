% Define the symbolic variable and function
syms x;
% Define the integrand
f = 2 * x * sqrt(x^2 + 1);
% Compute the integral
integral_result = int(f, x);
% Display the result
fprintf('The integral of the function is %s\n', ...
    char(integral_result));