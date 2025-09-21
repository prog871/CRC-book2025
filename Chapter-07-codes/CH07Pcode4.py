from sympy import symbols, laplace_transform, sin, exp
#
t, s = symbols('t s', real=True, positive=True)
#
f = sin(t)
F_shifted = laplace_transform(exp(2*t)*f, t, s)
print("Laplace of e^(2*t)*sin(t):", F_shifted)
