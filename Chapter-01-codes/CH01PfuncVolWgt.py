# Function to calculate volume and weight
def CH01PfuncVolWgt(L, W, H, gamma):
    """
    This function calculates volume and weight
    given length (L), width (W), height (H),
    and density (gamma). Dimensions are in
    meters and gamma in kg/m^3.
    """
    # Calculate volume (V_e = L*W*H)
    V_e = L * W * H  # volume in m^3
    # Calculate weight (Wgt = V_e*gamma)
    Wgt = V_e * gamma  # weight in kg
    return V_e, Wgt
