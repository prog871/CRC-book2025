from sympy import symbols, integrate
# Define the variable
x = symbols('x')
# Define the function
f = x**2
# Calculate the indefinite integral
indefinite_integral = integrate(f, x)
print("The indefinite integral of x^2 is:")
print(indefinite_integral)
# Calculate the definite integral
a = 0  # lower limit
b = 1  # upper limit
definite_integral = integrate(f, (x, a, b))
print(f"The definite integral of x^2 from {a} to \
{b} is {definite_integral}")
