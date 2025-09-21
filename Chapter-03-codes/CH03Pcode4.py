from sympy import symbols, diff
# Define the symbolic variable
t = symbols('t')
# Define the function f(t)
f = t**2 + t
# Calculate the derivative of f(t)
f_derivative = diff(f, t)
# Display the result
print(f"The derivative of f(t) is {f_derivative}")
