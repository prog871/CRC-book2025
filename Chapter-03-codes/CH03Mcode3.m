% Use symbolic math
syms x;
%
% Define the function
f = sin(x) / (x^2 + 1);
%
% Calculate the limit as x approaches 0
limit_value = limit(f, x, 0);
%
% Display the result
fprintf(['The limit of f(x) = sin(x) / (x^2 + 1) ' ...
    'as x approaches 0 is %.2f\n'], double(limit_value));