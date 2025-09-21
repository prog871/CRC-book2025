import numpy as np
from scipy.integrate import solve_ivp

def solve_ode1_numerical():
    """
    ODE: dy/dx = x^2, y(0) = 0
    Using solve_ivp for a numerical solution.
    """
    # Define the ODE function in the form f(t, y)
    def ode_func(t, y):
        # dy/dt = t^2
        return [t**2]

    # Integration interval
    x_span = (0, 2)
    # Initial condition (as a list/array of length 1)
    y0 = [0]

    # Points at which to store the solution
    t_eval = np.linspace(0, 2, 11)

    # Solve the ODE
    sol = solve_ivp(ode_func, x_span, y0, t_eval=t_eval)

    # Print results
    print("x values:", sol.t)
    print("y values:", sol.y[0])

    # Return the solution arrays
    return sol.t, sol.y[0]

if __name__ == "__main__":
    x_vals, y_vals = solve_ode1_numerical()
