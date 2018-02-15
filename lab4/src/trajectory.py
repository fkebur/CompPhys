#!/usr/bin/env python

from v3 import *
from cpode import *
from cpforces import *
from pylab import *
import math
import numpy as np
from scipy import optimize
from numpy.polynomial import polynomial as P        

def deltaX(angle):
    # Convention for the coordinates:
    #
    # x axis is horizontal, along the projectile motion.
    # y axis is vertical (directed upwards), and z axis makes
    # a left-handed coordinate system with x and y.

    # Projectile mass in kg( given as 4.0 g)
    m = 0.004 

    # Gravity force, and g
    Fg = ForceOfGravity(m)
    g = 9.81

    # Projectile x-sec area
    xsec = 2.43e-05

    # Air density
    Fp = 1.2

    # Initial elevation
    H = 1.0
        
    # Initial conditions
    x0 = V3(0.0, H, 0.0)
    speed = 930
    v0 = V3(speed*math.cos(angle), speed*math.sin(angle), 0.0)

    # Air drag, for first arg place magnitude of v0
    Fd = QuadraticDrag(xsec,Fp)

    # Prepare the ODE solver
    traj = RKF45(Fg+Fd, m)

    # different time deltas/colors.
    dt = 0.01

    # Cycle over time deltas and corresponding colors
    # Run the simulation
    traj.run(x0, v0, dt, AboveGround())

    # Extract the trajectory in the XY plane
    xcoords = np.array([vector.x for vector in traj.x])
    ycoords = np.array([vector.y for vector in traj.x])
    
    xshift = xcoords[-4:] - xcoords[-1]
    yshift = ycoords[-4:]  
    
    # Plot trajectories
    # plot(xcoords,ycoords)

    # Put a few finishing touches on the plot
    # title('Simulated Trajectories of a bullet shot from an M16 (%s Method)' % traj.name())
    # xlabel('X (m)')
    # ylabel('Y (m)')
    
    # Display the results
    # show()
    
    c = P.polyfit(xshift, yshift,4)
    roots = P.polyroots(c)
    xmax = roots[2] + xcoords[-1]
    return abs(xmax)

def negate(angle):
    return (-1)*(deltaX(angle))

maxAng = optimize.brent(negate,brack=(18*np.pi/180.0,42*np.pi/180.0))
print(maxAng)
