#
import sympy as sp
#
# Define the symbolic variable and function
x = sp.Symbol('x', real=True)
f = sp.exp(-x**2)
#
# Define the transform variable (commonly k or omega)
w = sp.Symbol('w', real=True)
#
# Compute the Fourier Transform of f(x)
# By default, sympy.fourier_transform uses the definition:
# F(k) = int f(x)*exp(-2*pi*i*x*k) dx
F = sp.fourier_transform(f, x, w)
#
# Compute the Inverse Fourier Transform
f_inverse = sp.inverse_fourier_transform(F, w, x)
#
# Print results
print("Fourier Transform of exp(-x^2):")
print(F)
print("\nInverse Fourier Transform of the above result:")
print(f_inverse)
