function solve_ode2_numerical
% ODE: y'' + 2y' + y = x^2,  y(0)=0, y'(0)=0.
% Convert to system of first order:
%   y1' = y2
%   y2' = x^2 - 2y2 - y1
odeFunc = @(x, Y)[ Y(2); x^2 - 2*Y(2) - Y(1) ];
Y0 = [0; 0];     % [y(0), y'(0)]
xspan = [0 2];
[xSol, YSol] = ode45(odeFunc, xspan, Y0);
ySol = YSol(:,1);
vSol = YSol(:,2);  % y' = v
% Display result
disp('Numerical solution (x, y, y''):');
result = table(xSol, ySol, vSol, 'VariableNames', ...
{'x','y','yprime'});
disp(result);
% Optional: plot
figure;
plot(xSol, ySol, 'o-');
xlabel('x');
ylabel('y');
title('Solution of y'''' + 2y'' + y = x^2');
end