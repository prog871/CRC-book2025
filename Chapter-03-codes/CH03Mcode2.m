% Use symbolic math
syms x;
%
% Define the function
f = 1 / x;
%
% Calculate the limit as x approaches 2
limit_value = limit(f, x, 2);
%
% Display the result
fprintf(['The limit of f(x) = 1/x as x ' ...
    'approaches 2 is %.2f\n'], double(limit_value));