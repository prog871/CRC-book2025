import sympy as sp
#
def solve_ode2_symbolic():
    """
    ODE: dy/dx + y = x^2, y(0) = 1
    Symbolic solution using sympy.
    """
    x = sp.symbols('x', real=True)
    y = sp.Function('y')
    ode = sp.Eq(sp.diff(y(x), x) + y(x), x**2)

    # Solve with initial condition y(0) = 1
    solution = sp.dsolve(ode, ics={y(0): 1})

    print("Symbolic solution for y(x):")
    print(solution)
#
if __name__ == "__main__":
    solve_ode2_symbolic()
