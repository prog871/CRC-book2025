from sympy import symbols, sin, cos, pi, integrate, simplify
#
# Define symbols
x, n = symbols('x n', real=True)
#
# Define the function
f = x
#
# 3. Compute a0
a0 = (1/pi) * integrate(f, (x, -pi, pi))
#
# 4. Define the Fourier coefficients
a_n = (1/pi) * integrate(f * cos(n*x), (x, -pi, pi))
b_n = (1/pi) * integrate(f * sin(n*x), (x, -pi, pi))
#
# 5. Build the N-term partial sum
N = 3
S = simplify(a0/2)              # start with the constant term
for k in range(1, N+1):
    ak = simplify(a_n.subs(n, k))
    bk = simplify(b_n.subs(n, k))
    S += ak * cos(k*x) + bk * sin(k*x)
#
print(f"The {N}-term Fourier series partial sum is:")
print(simplify(S))
