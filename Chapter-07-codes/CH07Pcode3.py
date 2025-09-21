from sympy import symbols, laplace_transform, sin
#
t, s = symbols('t s', real=True, positive=True)
#
f = t
g = sin(t)
#
Ff = laplace_transform(f, t, s)
Fg = laplace_transform(g, t, s)
F_combined = laplace_transform(2*f + 3*g, t, s)
#
print("Laplace of t:", Ff)
print("Laplace of sin(t):", Fg)
print("Laplace of 2*t + 3*sin(t):", F_combined)
