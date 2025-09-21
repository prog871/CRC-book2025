from sympy import symbols, laplace_transform, exp
#
t, s = symbols('t s', real=True, positive=True)
f = exp(2*t)  # f(t) = e^{2t}
#
F = laplace_transform(f, t, s)
print("Laplace Transform of exp(2*t):", F)
