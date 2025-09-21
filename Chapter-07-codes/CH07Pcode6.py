from sympy import symbols, inverse_laplace_transform
#
t, s = symbols('t s', real=True, positive=True)
F = 1/(s-3)
#
f = inverse_laplace_transform(F, s, t)
print("Inverse Laplace of 1/(s-3):", f)
