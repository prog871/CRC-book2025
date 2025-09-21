% Define symbolic variable and function
syms x;
f = exp(-x^2);
%
% Compute the Fourier Transform F(w) of f(x)
% By default, transforms with respect to e^(-i*x*w)
F = fourier(f, x);
disp('Fourier Transform of exp(-x^2):');
disp(F);
%
% Compute the Inverse Fourier Transform of F(w)
f_inverse = ifourier(F, x);
disp('Inverse Fourier Transform of the above result:');
disp(f_inverse);