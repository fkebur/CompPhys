import sys
#import NumDifferentiate 
import matplotlib.pyplot as plt
import numpy as np

# Set up and plot median relative error 
t = np.arange(10*sys.float_info.epsilon, 0.1, 1e-3)
med = np.median(t, out=1)
ax = plt.loglog(t, med)

plt.show()
