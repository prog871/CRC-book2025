syms s t
F = 1/s;
f = ilaplace(F, s, t);
disp("Inverse Laplace of 1/s = " + string(f))