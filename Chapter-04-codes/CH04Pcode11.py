import numpy as np
from scipy.integrate import solve_ivp
#
def solve_ode2_numerical():
    """
    ODE: y'' + 2y' + y = x^2,  y(0)=0,  y'(0)=0.
    Converted to first‑order system:
      Y = [y, v],
      Y' = [v,  x^2 - 2v - y].
    """
    def ode_system(t, Y):
        y, v = Y
        dydt = v
        dvdt = t**2 - 2*v - y
        return [dydt, dvdt]
#
    Y0 = [0, 0]                     # initial conditions: y(0)=0, y'(0)=0
    t_span = (0, 2)                 
    t_eval = np.linspace(0, 2, 11)  # 11 points between 0 and 2
#
    sol = solve_ivp(ode_system, t_span, Y0, t_eval=t_eval)
    if not sol.success:
        raise RuntimeError("ODE solver failed: " + sol.message)
#
    t_vals = sol.t
    y_vals = sol.y[0]
    v_vals = sol.y[1]
#
    print("t:", t_vals)
    print("y:", y_vals)
    print("y':", v_vals)
    return t_vals, y_vals, v_vals
#
if __name__ == "__main__":
    solve_ode2_numerical()

