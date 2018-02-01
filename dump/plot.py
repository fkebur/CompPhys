# Import all necessary names. Note that this, in general, is not a good
# programming style -- one can get in trouble with name collisions.
from numpy import *
from pylab import *

# Create an array of x values. The "linspace" function is defined
# in the "numpy" module. This function is inspired by MATLAB. To see
# more information about this function, type "?linspace" at the
# ipython prompt (without quotes). The navigation in this help system
# is performed by using space bar, "b", and "q", just like in the UNIX
# "man" command. To see exactly which submodule of "numpy" defines the
# "linspace" finction, type "print(linspace.__module__)" at the ipython
# prompt.
x = linspace(0, 2*pi, 100)

# Plot the graph of sin(x) vs. x. The "plot" function comes
# from the "pylab" module.
plot(x, sin(x))

# Add another graph
plot(x, cos(2*x))

# Label the horizontal axis of the graph
xlabel('x')

# Label the vertical axis
ylabel('sin(x) and cos(2x)')

# Display the plot on the screen
show()

# You can now click on the little cross at the top of the
# plot and then zoom/pan the resulting plot via the mouse.
# You can also save the plot as a an image file for subsequent
# inclusion into other documents.
