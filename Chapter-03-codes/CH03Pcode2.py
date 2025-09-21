# Import sympy
from sympy import symbols, limit
#
# Define the symbolic variable
x = symbols('x')
#
# Define the function
f = 1 / x
#
# Calculate the limit as x approaches 2
limit_value = limit(f, x, 2)
#
# Display the result
print("The limit of f(x) = 1/x as x \
approaches 2 is %.2f" % float(limit_value))
