from sympy import symbols, sin, cos, pi, integrate, simplify
#
# Define symbols
x, n = symbols('x n', real=True, integer=True)
#
# Define the function
f = x**2
#
# Compute a0
a0 = (1/pi) * integrate(f, (x, -pi, pi))
#
# Define a_n and b_n
a_n = (1/pi) * integrate(f * cos(n*x), (x, -pi, pi))
b_n = (1/pi) * integrate(f * sin(n*x), (x, -pi, pi))
#
# Build the partial sum (N = 3)
N = 3
S = a0/2
for k in range(1, N+1):
    ak = simplify(a_n.subs(n, k))
    # this will turn out to be 0 every time
    bk = simplify(b_n.subs(n, k))
    S = S + ak*cos(k*x) + bk*sin(k*x)
print(f"{N}-term Fourier series partial sum =", simplify(S))
