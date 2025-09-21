% Define the function
f = @(x) x + 1;
%
% Define the point of interest
x0 = 0;
%
% Calculate the limit
limit_value = f(x0);
%
% Display the result
fprintf( ['The limit of f(x) = x + 1 as x ' ...
    'approaches %d is %.2f\n'], x0, limit_value );
