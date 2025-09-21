import sympy
#
# Define symbols
x, y = sympy.symbols('x y', real=True)
#
# Define the temperature function T(x,y)
T = 18 - (3*x**2)/2 - y**2
#
# Compute partial derivatives
dTdx = T.diff(x)
dTdy = T.diff(y)
#
# Evaluate partial derivative w.r.t. x at (1,0)
val_dTdx_1_0 = dTdx.subs({x: 1, y: 0})
#
# Evaluate partial derivative w.r.t. y at (0,3)
val_dTdy_0_3 = dTdy.subs({x: 0, y: 3})
#
# Print results
print(f"dT/dx at (1,0) = {val_dTdx_1_0}")
print(f"dT/dy at (0,3) = {val_dTdy_0_3}")
