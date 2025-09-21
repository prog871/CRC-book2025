% Define the symbolic variable
syms x
% Define the function
f = x^2;
% Calculate the indefinite integral
indefinite_integral = int(f, x);
% Display the result
disp('The indefinite integral of x^2 is');
disp(indefinite_integral);
% Calculate the definite integral (example: from 0 to 1)
a = 0; % lower limit
b = 1; % upper limit
definite_integral = int(f, x, a, b);
% Display the result
fprintf( ...
  ['The indefinite integral of x^2 is %s, ' ...
   'and the definite integral from %d to %d is %s\n'], ...
  char(indefinite_integral), a, b, char(definite_integral) ...
);