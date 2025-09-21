syms x n real
f = x;  % Define the function
%
% Compute a0
a0 = (1/pi) * int(f, x, -pi, pi);
%
% Define a_n and b_n as symbolic expressions
a_n = (1/pi) * int(f .* cos(n*x), x, -pi, pi);
b_n = (1/pi) * int(f .* sin(n*x), x, -pi, pi);
%
% Build the partial sum (N=3)
N = 3;
S = a0/2;   % Start with a0/2
%
for k = 1:N
    ak = simplify(subs(a_n, n, k));
    bk = simplify(subs(b_n, n, k));
    S  = S + ak*cos(k*x) + bk*sin(k*x);
end
%
disp(['The ', num2str(N), ...
'-term Fourier series partial sum is:']);
S_simplified = simplify(S);
disp(S_simplified);