#!/usr/bin/env python
#
# You can get a description of the GridFill2d functionality
# at the interactive python prompt in the usual manner:
#
# from GridFill2d import *
# help(GridFill2d)

from pylab import *
from GridFill2d import *
import numpy as np

# set up grid
g = GridFill2d(100, 0, 30, 100, 0, 30, 0, True)

# set up a boundary where voltage is 100 
assert g._setHorizontal(10, 20, 12, -100)
assert g._setHorizontal(10, 20, 18, 100)

# use SOR to fill grid around capacitor plates
w = 2/(1 + np.pi/100)
g.SOR(200, w)

# Plot the grid values using a color map
fig = figure()
ax = fig.add_subplot(211)
mshow = ax.matshow(g.data)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.xaxis.set_label_position('top')
fig.colorbar(mshow, aspect=10)

#######################################################

# Plot iteration for convergence vs w
omega = [1,1.2,1.4,1.6,1.8,1.9,2]

ax1 = fig.add_subplot(212)


for i in omega:
	for j in range(100):
		checknum = g.SOR(j,i)
		if checknum == -5.24598181061:
			ax1.plot(j,i,'.-')
		else:
			continue


ax1.set_xlabel('$\omega$')
ax1.set_ylabel('Number of iterations')



show()
