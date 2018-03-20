#!/usr/bin/python

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# original seed and small changed seed
x0 = 0.75
x1 = 0.75001

# mu values
µ = [3.3, 3.8]

# logistic map function
def logmap(m,x):
	return m*x*(1-x)

# 1st line(µ = 3.3) y-value initialization
y0 = []
y1 = []
N = 101 

# fill arrays with x, and y values
for n in range(N):
    x0 = logmap(µ[0],x1)
    x1 = logmap(µ[1],x1)
    y0.append(x0)
    y1.append(x1)

# calculate difference in logistic map values for x
diff0 = np.zeros(len(y0))
diff1 = np.zeros(len(y0))

for i in np.arange(1, len(y0)-1):
    diff0[i] = y0[i+1]-y0[i]
    diff1[i] = y1[i+1]-y0[i]

ab_diff0 =abs(diff0)
ab_diff1 =abs(diff1)

'''

diff0 = [a - b for a,b in zip(y1,y0)]
ab_diff0 = list(map(abs,diff0))

# fill arrays with x, and y values
for n in range(N):
    x0 = logmap(µ[0],x1)
    x1 = logmap(µ[1],x1)
    l0.append(x0)
    l1.append(x1)

diff1 = [a - b for a,b in zip(l1,l0)]
ab_diff1 = list(map(abs,diff1))

'''

# plot logistic maps
plt.semilogy(range(N), ab_diff0)
plt.semilogy(range(N), ab_diff1)
plt.title('Logistic maps')
plt.legend(['µ = 3.3', 'µ = 3.5'], loc='upper right')
plt.xlabel('i')
plt.ylabel("|X_i'-X_i|")
plt.show()

'''

# test range
#µR = np.arange(1,1.5,.01)

# range of µ from 1 to 4 in 1000 steps
µRange = np.arange(1, 4, 0.003)

# range of x0 values 
xRange = np.arange(0, 1, 0.001)

# generation # range
I = 201
Irang0 = range(1, I, 1)
Irang1 = range(I, 402, 1)

count = 0
rmDbl = int(1000*0.5)


for µ in µRange:
    
    y = 0.5

    # skip transients
    for i in Irang0:
        y = logmap(µ, y)
    for i in Irang1:
        y = logmap(µ, y)
    for i in Irang1:
        
        # avoid doubles
        oldy = int(1000 * y)
        y = logmap(µ, y)
        inty = int(1000 * y)
        if inty != rmDbl and count%2 == 0:
            plt.plot(µ, y,'co')
    
    rmDbl = inty
    count += 1

# set plot limits
xmin = 1
ymax = 1
xmax = 4
ymin = 0

axes = plt.gca()
axes.set_xlim([xmin,xmax])
axes.set_ylim([ymin,ymax])

# show figure
#plt.show()
'''
