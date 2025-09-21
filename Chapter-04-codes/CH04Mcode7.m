function solve_ode2_numerical
% ODE: y'(x) + y(x) = x^2, y(0) = 1
% Numerical solution with ode45.
%  
% Define the ODE: y'(x) = x^2 - y(x)
odeFunc = @(x,y) x.^2 - y;
xspan = [0 2];  % example interval
y0 = 1;         % initial condition
%    
[xSol, ySol] = ode45(odeFunc, xspan, y0);
% Display the results
disp('Numerical solution (x, y):');
result = table(xSol, ySol, 'VariableNames', {'x','y'});
disp(result);
% Optional plotting
plot(xSol, ySol, 'o-');
title('Numerical Solution of y''(x) + y(x) = x^2');
xlabel('x');
ylabel('y');
end