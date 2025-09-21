from sympy import symbols, exp, integrate
# Define the symbolic variable
x = symbols('x')
# Define the function
f = x * exp(x)
# Calculate the integral
integral_result = integrate(f, x)
# Display the result
print(f"The integral of the function x*e^x \
is {integral_result}")
