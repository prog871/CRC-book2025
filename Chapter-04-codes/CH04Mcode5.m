function solve_ode1_numerical
% ODE: y'(x) = x^2, y(0) = 0
% Using ode45 for a numerical solution.
% Define the ODE as a function handle
% dydx = x^2
odeFunc = @(x,y) x.^2;
%
% Define the interval of integration and the initial condition
xspan = [0 2];    % Solve from x=0 to x=2 (example interval)
y0 = 0;           % y(0) = 0
%    
% Call ode45
[xSol,ySol] = ode45(odeFunc, xspan, y0);
%   
% Display the results
disp('Numerical solution (x, y):');
result = table(xSol, ySol, 'VariableNames', {'x','y'});
disp(result);
%   
% Optional: plot the solution
plot(xSol, ySol, 'o-');
title('Numerical Solution of y''(x) = x^2');
xlabel('x');
ylabel('y');
end