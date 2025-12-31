import numpy as np

def get_circumcenter(A, B, C):
    # Matrix of the system: 2*(B-A) and 2*(C-A)
    M = 2 * np.array([B - A, C - A])
    
    # Check the determinant (cross product in 2D)
    # det = 2(Bx-Ax)*2(Cy-Ay) - 2(By-Ay)*2(Cx-Ax)
    det = np.linalg.det(M)
    
    if np.isclose(det, 0):
        return None  # Or raise a specific ValueError
    
    # RHS of the equation: |B|^2 - |A|^2 and |C|^2 - |A|^2
    v = np.array([
        np.dot(B, B) - np.dot(A, A),
        np.dot(C, C) - np.dot(A, A)
    ])
    
    # Solve for P(x, y)
    return np.linalg.solve(M, v)

# Testing
A, B, C = np.array([0,0]), np.array([3,1]), np.array([0,2])
center = get_circumcenter(A, B, C)

if center is not None:
    print(f"Circumcenter: {center}")
else:
    print("Points are collinear.")
