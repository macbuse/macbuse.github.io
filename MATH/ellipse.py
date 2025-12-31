import numpy as np


def get_ellipse_params(coeffs):
    """
    Input: coeffs = [A, B, C, D, E, F] 
    for Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
    """

    A, B, C, D, E, F = coeffs
    # Calculate the center of the get_ellipse_params get_ellipse_params     
    denom = B**2 - 4*A*C
    x0 = (2*C*D - B*E) / denom
    y0 = (2*A*E - B*D) / denom
    center = np.array([x0, y0])
    # Calculate the axes lengths
    numerator = 2 * (A*E**2 + C*D**2 - B*D*E + denom*F)
    term = np.sqrt((A - C)**2 + B**2)
    a_length = np.sqrt(numerator / (denom * (A + C + term)))
    b_length = np.sqrt(numerator / (denom * (A + C - term)))
    axes = np.array([a_length, b_length])
    # Calculate the rotation angle
    if B == 0 and A < C:
        angle = 0
    elif B == 0 and A >= C:
        angle = np.pi / 2
    else:
        angle = 0.5 * np.arctan2(B, A - C)  

    return {"ce" : center, 
            "w": a_length, "h" : b_length, 
            "rot": angle}
