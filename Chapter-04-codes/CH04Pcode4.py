from sympy import symbols, sin, integrate
#
# Define symbols
x, y, z = symbols('x y z')
#
# Define the integrand
integrand = x**2 + y*sin(z)
#
# Perform the integrations step by step
# Integrate w.r.t x from 0 to 1
inner_integral = integrate(integrand, (x, 0, 1))
# Integrate w.r.t y from 0 to 2
middle_integral = integrate(inner_integral, (y, 0, 2))
# Integrate w.r.t z from 0 to 3
outer_integral = integrate(middle_integral, (z, 0, 3))
#
# Print the result
print(f"The value of the triple integral is: \
{float(outer_integral)}")
