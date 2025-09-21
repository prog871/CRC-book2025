import numpy as np
from scipy.integrate import solve_ivp
#
def solve_ode1_numerical():
    """
    ODE: y''(x) = 6x, with y(0)=2, y'(0)=1.
    Convert to system of first order:
      y'(x) = v
      v'(x) = 6x
    """
    def ode_system(x, Y):
        y, v = Y
        return [v, 6*x]
#
    # Initial conditions
    Y0 = [2, 1]       # [y(0), v(0)=y'(0)]
    # Domain and output points
    x_span = (0, 2)
    t_eval = np.linspace(0, 2, 11)
#
    # Solve the system
    sol = solve_ivp(ode_system, x_span, Y0, t_eval=t_eval)

    # Unpack
    x_vals = sol.t
    y_vals = sol.y[0]
    v_vals = sol.y[1]
#
    # Show
    print("x values:", x_vals)
    print("y values:", y_vals)
    print("v = y' values:", v_vals)

    return x_vals, y_vals, v_vals
#
if __name__ == "__main__":
    solve_ode1_numerical()
