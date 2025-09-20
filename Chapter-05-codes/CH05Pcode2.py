# This code finds the flow depth (y) 
# in a channel # based on Manning's
# equation using 'Bisection Method'
import math
def f(y):
  return (1/0.013)*3*y*((3*y)\
   /(3+2*y))**(2/3)*math.sqrt(0.001)-10
# Initial interval
a = 0.1; b = 4
tol = 0.001  # Tolerance for stopping
X2= 100  # Maximum iterations
# Check if initial interval is valid
if f(a) * f(b) > 0:
 raise ValueError("No root in [a, b]")
# Bisection Method
iter_count = 0
while (b - a) / 2 > tol:
    c = (a + b) / 2  # Midpoint
    fc = f(c)
    # Check if midpoint is the root
    if abs(fc) < tol:
        break
    elif f(a)*fc<0: b=c  #Root in [a,c]
    else: a = c  # Root in [c,b]
    iter_count += 1
    if iter_count > X2:
        raise ValueError("Maximum iterations reached")
root = (a + b) / 2  # Final root
# Display results
print(f"Root found: y = {root:.4f}")
print(f"f(y) at root is {f(root):.4f}")
# End of Python script
