% For a second order ODE, we typically reduce it to a system of two first-order ODEs:
% Let v(x) = y'(x). Then dv/dx=6x. So we have:
% y'(x) = v(x) & v'(x) = 6x with y(0)=2 & v(0)=1.
%
function solve_ode1_numerical
% ODE: y''(x) = 6x, with y(0)=2, y'(0)=1.
% Convert to system: 
%   y'(x) = v(x)
%   v'(x) = 6x
% System function
% State vector: Y = [ y; v ]
% Y'(x) = [ v; 6x ]
odeFunc = @(x,Y) [Y(2); 6*x];
% Initial conditions
y0 = 2;    % y(0)
v0 = 1;    % y'(0)
Y0 = [y0; v0];
% Interval of integration
xspan = [0 2];
% Solve numerically
[xSol, YSol] = ode45(odeFunc, xspan, Y0);
% YSol(:,1) = y values, YSol(:,2) = v (= y') values
ySol = YSol(:,1);
vSol = YSol(:,2);
% Display the results
disp('Numerical solution (x, y, y'') in terms of (x, y, v):');
result = table(xSol, ySol, vSol, 'VariableNames', ...
{'x','y','v'});
disp(result);
% Optional: plot the solution for y(x)
figure;
plot(xSol, ySol, 'o-');
title('Numerical Solution of y''''(x) = 6x');
xlabel('x');
ylabel('y');
end