import numpy as np
from scipy.integrate import solve_ivp

def solve_ode2_numerical():
    """
    ODE: dy/dx + y = x^2, y(0) = 1
    Rewritten as dy/dx = x^2 - y.
    """
    # Define the right‑hand side f(t, y)
    def ode_func(t, y):
        return t**2 - y

    # Integration interval and initial condition
    t_span = (0, 2)
    y0 = [1]

    # Points at which to store the solution
    t_eval = np.linspace(0, 2, 11)

    # Solve!
    sol = solve_ivp(ode_func, t_span, y0, t_eval=t_eval)

    # Report results
    print("t values:", sol.t)
    print("y values:", sol.y[0])
    return sol.t, sol.y[0]

if __name__ == "__main__":
    solve_ode2_numerical()
