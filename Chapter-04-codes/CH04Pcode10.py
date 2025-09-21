import sympy as sp
#
def solve_ode1_symbolic():
    """
    ODE: y''(x) = 6x,  y(0)=2, y'(0)=1
    Use sympy.dsolve to get a symbolic solution.
    """
    x = sp.symbols('x', real=True)
    y = sp.Function('y')(x)
#
    # Define the ODE y'' = 6*x
    ode_equation = sp.Eq(y.diff(x, 2), 6*x)
#
    # Solve with initial conditions y(0)=2, y'(0)=1
    sol = sp.dsolve(ode_equation,
                    ics={y.subs(x, 0): 2,
                         y.diff(x).subs(x, 0): 1})
#
    print("Symbolic solution for y(x):")
    print(sol)  # prints: Eq(y(x), x**3 + x + 2)
#
if __name__ == "__main__":
    solve_ode1_symbolic()
