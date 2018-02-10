# Comp. Physics
# Kebur Fantahun
#Lab 1 - Part 3 and 4
# Show that a certain algorithm is error ridden and attempt to improve upon it

import numpy as np
import numpy.linalg as la
import vectangle


u = np.array([1,2])
v = np.array([2,4])

norm_u = la.norm(u)
norm_v = la.norm(v)

dotp = np.dot(u,v)

alpha = np.arccos(dotp/(norm_u*norm_v))

new_alpha = vectangle.VectorAngle(u,v)

print('The error ridden algorithm tells us the angle between u and v is ',alpha)

print('\n' + 'My method says the angle is ',str(new_alpha))	

