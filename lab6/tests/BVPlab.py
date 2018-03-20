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

# set up a boundary where voltage is 0 
assert g._setHorizontal(10, 20, 11, 100)
assert g._setHorizontal(10, 20, 19, -100)

# use SOR to fill grid around capacitor plates
w = 1
g.SOR(300, w)

# Plot the grid values using a color map
fig = figure()
ax = fig.add_subplot(111)
mshow = ax.matshow(g.data)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.xaxis.set_label_position('top')
fig.colorbar(mshow, aspect=10)

show()
