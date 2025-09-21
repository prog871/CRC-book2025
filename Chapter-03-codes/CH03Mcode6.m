% Define the symbolic variable
syms x;
% Define the function
f = x^3 / (x^2 + 1);
% Calculate the derivative
f_prime = diff(f, x);
% Display the result
fprintf('The derivative of f(x) is %s\n', char(f_prime));