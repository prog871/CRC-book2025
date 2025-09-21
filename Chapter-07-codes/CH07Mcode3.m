syms t s
f = t;
g = sin(t);
%
Ff = laplace(f, t, s);
Fg = laplace(g, t, s);
F_combined = laplace(2*f + 3*g, t, s);
%
disp("Laplace of t = " + string(Ff))
disp("Laplace of sin(t) = " + string(Fg))
disp("Laplace of 2*t + 3*sin(t) = " + string(F_combined))