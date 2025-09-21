% Define the symbolic variable
syms x
% Define the function
f = x * exp(x);
% Calculate the integral
integral_result = int(f, x);
% Display the result
fprintf('The integral of x*e^x is %s\n', ...
    char(integral_result));