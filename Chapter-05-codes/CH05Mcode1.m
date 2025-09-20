% This code finds the roots
% of: f(x) = x^2 - 2x -3
% using 'Bisection Method'
clc; clear; close all;
f = @(x) x^2 - 2*x - 3;
% First root in interval [0,4]
a1 = 0; b1 = 4;
tol=1e-6; %Tolerance for stopping
X2= 500; % Maximum iterations
% Bisection Method for first root
iter = 0;
while (b1 - a1) / 2 > tol
    c1 = (a1 + b1) / 2;
    if f(c1) == 0; break;
    elseif f(a1) * f(c1) < 0; b1=c1;
    else; a1 = c1;
    end
    iter = iter + 1;
    if iter > X2
     disp('Max iterations');break;
    end
end
root1 = (a1 + b1) / 2;
disp(['First root: ',num2str(root1)]);
% Second root in the interval [-4,0]
a2 = -4; b2 = 0; iter = 0;
while (b2 - a2) / 2 > tol
    c2 = (a2 + b2) / 2;
    if f(c2) == 0; break;
    elseif f(a2)*f(c2)<0; b2=c2;
    else; a2 = c2;
    end
    iter = iter + 1;
    if iter > X2
      disp('Max iterations');break;
    end
end
root2 = (a2 + b2) / 2;
disp(['Second root: ',num2str(root2)]);
% end of M - file
