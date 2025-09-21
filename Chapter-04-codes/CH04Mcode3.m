syms x y z
%
%% 1) Single integral
integrand_single = x^2 + 3;
result_single = int(integrand_single, x, 0, 2);
%
%% 2) Double integral
integrand_double = x*y + exp(x);
% Integrate w.r.t y
inner_double = int(integrand_double, y, 0, 2);
% Integrate w.r.t x
result_double = int(inner_double, x, 0, 1);
%
%% 3) Triple integral
integrand_triple = exp(x + y + z);
% Integrate w.r.t x
inner_triple = int(integrand_triple, x, 0, 1);
% Integrate w.r.t y
middle_triple = int(inner_triple, y, 0, 2);  
% Integrate w.r.t z
result_triple = int(middle_triple, z, 0, 3); 
%
%% Display symbolic results
disp('Symbolic results:')
disp(['1) Single integral  = ', char(result_single)]);
disp(['2) Double integral  = ', char(result_double)]);
disp(['3) Triple integral  = ', char(result_triple)]);
%
%% Display numerical approximations
disp(' ')
disp('Numerical approximations:')
disp(['1) Single integral ~= ', ...
num2str(double(result_single))]);
disp(['2) Double integral  ~= ', ...
num2str(double(result_double))]);
disp(['3) Triple integral  ~= ', ...
num2str(double(result_triple))]);