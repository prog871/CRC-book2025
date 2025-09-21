from sympy import symbols, exp, integrate
#
# Define the symbols
x, y, z = symbols('x y z', real=True)
#
# 1) Single integral
integrand_single = x**2 + 3
result_single = integrate(integrand_single, (x, 0, 2))
#
# 2) Double integral
integrand_double = x*y + exp(x)
# Integrate w.r.t y
inner_double = integrate(integrand_double, (y, 0, 2))
# Integrate w.r.t x
result_double = integrate(inner_double, (x, 0, 1)) 
#
# 3) Triple integral
integrand_triple = exp(x + y + z)
# Integrate w.r.t x
inner_triple = integrate(integrand_triple, (x, 0, 1))
# Integrate w.r.t y
middle_triple = integrate(inner_triple, (y, 0, 2))
# Integrate w.r.t z
result_triple = integrate(middle_triple, (z, 0, 3))
#
# Print symbolic results
print("Symbolic results:")
print(f"1) Single integral  = {result_single}")
print(f"2) Double integral  = {result_double}")
print(f"3) Triple integral  = {result_triple}")
#
# Print numerical approximations
print("\nNumerical approximations:")
print(f"1) Single integral  ~= {float(result_single.evalf())}")
print(f"2) Double integral  ~= {float(result_double.evalf())}")
print(f"3) Triple integral  ~= {float(result_triple.evalf())}")
