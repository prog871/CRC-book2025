syms t s
f = sin(t);
%
F_shifted = laplace(exp(2*t)*f, t, s);
disp("Laplace of e^(2*t)*sin(t) = " + string(F_shifted))