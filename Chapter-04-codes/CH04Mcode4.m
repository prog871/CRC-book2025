% MATLAB script to evaluate the triple integral
syms x y z;
% Define the integrand
integrand = x^2 + y*sin(z);
%
% Perform the integrations step by step
% Integrate w.r.t x from 0 to 1
inner_integral = int(integrand, x, 0, 1); 
% Integrate w.r.t y from 0 to 2
middle_integral = int(inner_integral, y, 0, 2);
% Integrate w.r.t z from 0 to 3
outer_integral = int(middle_integral, z, 0, 3);
%
% Display the result
disp('The value of the triple integral is:');
disp(double(outer_integral));