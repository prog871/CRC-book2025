% Fourier series of x^2 on [-pi,pi], first 3 terms
syms x
%
% Define the function
f = x^2;
%
% Compute the a0 coefficient
a0 = (1/pi)*int(f, x, -pi, pi);    % a0 = 2*pi^2/3
%
% Number of harmonics
N = 3;
%
% Preallocate arrays for a_n, b_n
an = sym(zeros(1,N));
bn = sym(zeros(1,N));
%
% Compute a_n and b_n for n=1..3
for n = 1:N
    an(n) = (1/pi)*int( f*cos(n*x), x, -pi, pi );
    bn(n) = (1/pi)*int( f*sin(n*x), x, -pi, pi );
end
%
% Simplify coefficients
a0 = simplify(a0);
an = simplify(an);
bn = simplify(bn);
%
% Build the 3-term Fourier series
f3 = a0/2;
for n = 1:N
    f3 = f3 + an(n)*cos(n*x) + bn(n)*sin(n*x);
end
f3 = simplify(f3);
%
% Show the approximation
disp('3-term Fourier approximation:');
disp(f3)