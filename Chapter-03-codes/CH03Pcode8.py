from sympy import symbols, integrate, sqrt
# Define the symbolic variable
x = symbols('x')
# Define the integrand
f = 2 * x * sqrt(x**2 + 1)
# Compute the integral
integral_result = integrate(f, x)
# Display the result
print(f"The integral of the function is \
{integral_result}")
