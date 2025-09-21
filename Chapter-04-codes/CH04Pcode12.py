import sympy as sp
#
def solve_ode2_symbolic():
    """
    ODE: y'' + 2y' + y = x^2, y(0)=0, y'(0)=0
    Use sympy to solve symbolically.
    """
    # Declare symbols and function
    x = sp.Symbol('x', real=True)
    y = sp.Function('y')(x)
#
    # Define the ODE
    ode_equation = sp.Eq(y.diff(x, 2) + 2*y.diff(x) + y, x**2)
#
    # Solve with initial conditions
    sol = sp.dsolve(
        ode_equation,
        ics={
            y.subs(x, 0): 0,
            y.diff(x).subs(x, 0): 0
        }
    )
#
    print("Symbolic solution for y(x):")
    print(sol)
#
if __name__ == "__main__":
    solve_ode2_symbolic()
