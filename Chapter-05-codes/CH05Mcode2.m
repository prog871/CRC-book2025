% This code finds the flow
% depth (y) in a channel
% based on Manning's equation 
% using 'Bisection Method'
clc; clear; close all;
% Define the function
f = @(y) (1/0.013) * 3 * y *...
((3 * y) / (3 + 2 * y))^(2/3) *...
sqrt(0.001) - 10;
% Initial interval
a = 0.1; b = 4;
tol = 0.001; % Tolerance for stopping
X2 = 100; % Maximum iterations
% Check if initial interval is valid
if f(a) * f(b) > 0
    error('No root in [a, b]');
end
iter = 0;
while (b - a) / 2 > tol
  c = (a + b) / 2; fc = f(c);
  % Check if midpoint is the root
  if abs(fc) < tol; break;
  elseif f(a)*fc<0; b=c; %Root in [a,c]
  else  a = c; % Root in [c,b]
  end
    iter = iter + 1;
  if iter>X2; error('Max iterations');
  end
end
root=(a+b)/2; %Final root approximation
% Display results
fprintf('Root found: y = %.4f \n',root);
fprintf('f(y) at root is %.4f\n',f(root));
% end of M - file
