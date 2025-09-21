# Import sympy
from sympy import symbols, sin, limit
#
# Define the symbolic variable
x = symbols('x')
#
# Define the function
f = sin(x) / (x**2 + 1)
#
# Calculate the limit as x approaches 0
limit_value = limit(f, x, 0)
#
# Display the result
print(f"The limit of f(x) = sin(x) / (x^2 + 1) as x \
approaches 0 is {float(limit_value):.2f}")
