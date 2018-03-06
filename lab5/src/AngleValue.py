#!/usr/bin/python

import numpy as np
from cpode import *
from physical_pendulum import *

def AngleValue(theta0, F_D):
    
    # System Parameters
    omega0 = 1.0
    dissipationCoefficient = 0.5
    omegaD = 2.0/3.0
    periodD = 2*np.pi/omegaD

    # Prepare the force model
    force = DrivenPendulum(omega0, dissipationCoefficient, F_D, omegaD)

    # Prepare the ODE solver
    pendulum = RK4(force)

    # Initial conditions
    omegaInitial = 0.0

    # Simulation time step
    dt = 0.04

    # Simulation stopping condition
    whenToStop = TimeLimit(400*periodD)

    # Run the simulation
    pendulum.run(theta0, omegaInitial, dt, whenToStop)

    # skip the first 200 periods
    periodRange = np.arange(200*periodD,400*periodD,periodD)
    angle = []

    for t in periodRange:
        x, v = pendulum.interpolate(t)
        angle.append(standard_angle(x))

    return angle
