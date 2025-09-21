import sympy
#
# Define symbols
x, y = sympy.symbols('x y', real=True)
#
# Define the function T(x,y)
T = x*sympy.exp(y) + y*sympy.sin(x)
#
# Compute partial derivatives
dTdx = T.diff(x)  # Partial derivative w.r.t. x
dTdy = T.diff(y)  # Partial derivative w.r.t. y
#
# Evaluate partial derivative w.r.t. x at (2,1)
val_dTdx_2_1 = dTdx.subs({x: 2, y: 1})
#
# Evaluate partial derivative w.r.t. y at (1,2)
val_dTdy_1_2 = dTdy.subs({x: 1, y: 2})
#
# Convert to a numerical approximation
val_dTdx_2_1_num = val_dTdx_2_1.evalf()
val_dTdy_1_2_num = val_dTdy_1_2.evalf()
#
# Print results
print(f"dT/dx at (2,1) = {val_dTdx_2_1_num}")
print(f"dT/dy at (1,2) = {val_dTdy_1_2_num}")
