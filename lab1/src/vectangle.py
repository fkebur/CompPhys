import numpy as np
import numpy.linalg as la

def VectorAngle(v1, v2):
    # Returns the angle in radians between vectors 'v1' and 'v2'
    cos_angle = np.dot(v1, v2)
    sin_angle = la.norm(np.cross(v1, v2))
    
    return np.arctan2(sin_angle, cos_angle)
