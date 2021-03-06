#!/usr/bin/env python

from cpode import *
from physical_pendulum import *
import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import math

# System parameters
omega0 = 1.0
dissipationCoefficient = 0.5
F_D = 1.5
omegaD = 2.0/3.0

# Prepare the force model
force = DrivenPendulum(omega0, dissipationCoefficient, F_D, omegaD)

# Prepare the ODE solver
pendulum = RK4(force)

# Initial conditions
thetaInitial = 0.1
omegaInitial = 0.0

# Simulation time step
dt = 0.04

# Simulation stopping condition
whenToStop = TimeLimit(300)

# Run the simulation
pendulum.run(thetaInitial, omegaInitial, dt, whenToStop)

# Plot figure
figure()

# Plot the angle vs. time
subplot(221)
plot(pendulum.t, pendulum.x, linewidth=1.0)
title('Pendulum Angle vs. Time')
xlabel('Time (s)')
ylabel('Angle (radians)')

# Plot the phase space diagram
subplot(222)
plot(pendulum.x, pendulum.v, linewidth=1.0)
title('Pendulum Phase Space Diagram')
xlabel('Angle (radians)')
ylabel('Angular Velocity (radians/s)')

# Plot the reduced phase space diagram in which all
# angles are inside the range (-Pi, Pi)
subplot(223)
angles = [standard_angle(a) for a in pendulum.x]
plot(angles, pendulum.v, linewidth=1.0)
title('Reduced Pendulum Phase Space Diagram')
xlabel('Angle (radians)')
ylabel('Angular Velocity (radians/s)')

# Plot the Poincare section
npoints = 200
period = 2*math.pi/omegaD
pendulum.run(thetaInitial, omegaInitial, dt, TimeLimit(period*(npoints+1)))
theta = []
omega = []
for i in range(npoints):
    x, v = pendulum.interpolate(period*i)
    theta.append(standard_angle(x))
    omega.append(v)

subplot(224)
scatter(theta, omega)
title('Pendulum Poincare Section')
xlabel('Angle (radians)')
ylabel('Angular Velocity (radians/s)')

suptitle('Driving Force = {:.2f}'.format(F_D), fontsize=14)
subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)

# Display the results
show()
