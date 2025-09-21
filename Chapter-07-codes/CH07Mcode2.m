syms t s
f = exp(2*t);           
F = laplace(f, t, s)     % Compute Laplace transform of exp(2*t)