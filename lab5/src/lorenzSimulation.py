#!/usr/bin/env python

from v3 import V3
from cpode import *
from LorenzModel import LorenzEffectiveForce
from pylab import *
import math

# System parameters are taken from the original study by Lorentz
sigma = 10.0
b = 8.0/3.0
rValues    = (10.0, 24.0, 25.0)
plotcolors = ('g',  'r',  'b')

# System initial conditions
xInitial = V3(0.0, 0.0, 0.0)
vInitial = V3(1.0, 0.0, 0.0)

# Simulation time step
dt = 0.005

# Simulation stopping condition
whenToStop = TimeLimit(100)

# Plot the z component of the velocity vs. x component
ax1 = figure().add_subplot(111)
title('Phase space diagram: z vs. x')
xlabel('x')
ylabel('z')

# Plot the y component of the velocity vs. x component
ax2 = figure().add_subplot(111)
title('Phase space diagram: y vs. x')
xlabel('x')
ylabel('y')

text_position = 0.9

# Run the simulation
for r, color in zip(rValues, plotcolors):
    # Prepare the force model
    force = LorenzEffectiveForce(sigma, r, b)

    # Prepare the ODE solver
    lorenzModel = RK4(force)

    # Run the simulation
    lorenzModel.run(xInitial, vInitial, dt, whenToStop)

    # Plot the results
    vx = [v.x for v in lorenzModel.v]
    vy = [v.y for v in lorenzModel.v]
    vz = [v.z for v in lorenzModel.v]
    ax1.plot(vx, vz, linewidth=1.0, color=color)
    ax2.plot(vx, vy, linewidth=1.0, color=color)

    # Put a label on the plot which shows r with the same color
    # as the plot line
    for ax in (ax1, ax2):
        ax.text(0.45, text_position, "r = %r" % r, color=color,
                transform = ax.transAxes)
    text_position -= 0.07

# Display the results
show()
