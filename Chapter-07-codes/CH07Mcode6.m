syms s t
F = 1/(s-3);
f = ilaplace(F, s, t);
disp("Inverse Laplace of 1/(s-3) = " + string(f))