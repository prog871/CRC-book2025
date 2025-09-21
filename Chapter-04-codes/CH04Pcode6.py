import sympy as sp
#
def solve_ode1_symbolic():
    """
    ODE: dy/dx = x^2, y(0) = 0
    Using sympy.dsolve for a symbolic solution.
    """
    x = sp.Symbol('x', real=True)
    y = sp.Function('y')(x)

    # Define the ODE
    ode_equation = sp.Eq(sp.diff(y, x), x**2)

    # Solve with the initial condition y(0)=0
    solution = sp.dsolve(ode_equation, ics={y.subs(x, 0): 0})

    print("Symbolic solution for y(x):")
    print(solution)
#
if __name__ == "__main__":
    solve_ode1_symbolic()
