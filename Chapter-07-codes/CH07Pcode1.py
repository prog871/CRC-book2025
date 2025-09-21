from sympy import symbols, laplace_transform
#
t, s = symbols('t s', real=True, positive=True)
f = 1  # Define f(t) = 1
#
F = laplace_transform(f, t, s)
print("Laplace Transform of 1:", F)
