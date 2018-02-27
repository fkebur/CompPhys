#!/usr/bin/python

import matplotlib.pyplot as plt

# The seed, or x0, is 0.75

mu = 3.828427
def logmap(x):
	return mu*x*(1-x)

# y-value(s) initialization

y = []
N = 101 
x = 0.75

for n in range(N):
	y.append(x)
	x = logmap(x)

plt.plot(range(N),y)
plt.show()
