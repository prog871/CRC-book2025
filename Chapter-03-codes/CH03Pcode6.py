from sympy import symbols, diff
# Define the symbolic variable
x = symbols('x')
# Define the function
f = x**3 / (x**2 + 1)
# Calculate the derivative
f_prime = diff(f, x)
# Display the result
print(f"The derivative of f(x) is {f_prime}")
