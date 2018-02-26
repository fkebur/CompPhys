#!/usr/bin/python

import numpy as np
import math
import sys
import matplotlib.pyplot as plt
import gaussLegendreQuadrature as glq

eps = sys.float_info.epsilon

'''
This section defines functions trapz and simpsons to take integral approximations
'''

def trapz(f, N, xmin, xmax):
    """ 
    This function performs an integral approximation with the so-called trapezoidal rule. Arguments are
    as follows:

    f          -- The function (callable) to integrate. It will be called
                  with one argument.
    N          -- Number of points to use for integration. Call "validNValues()"
                  function to find out which values of N are supported.
    xmin, xmax -- Integration interval.
    """
    # Calculate h value
    h = (xmax - xmin)/(N + eps)
    
    # Computing sum of first and last terms
    # in above formula
    tot = (f(xmin) + f(xmax))
    
    # Sum up the remaining terms
    i = 1
    
    while i < n:
        tot += 2 * f(xmin + i * h)
        i += 1
    
    # h/2 = (xmax-xmin)/2n. 
    # Multiplying h/2 with tot gives back h.
    return ((h / 2) * tot)

def simpsons(f, N, xmin ,xmax ):
    """ 
    This function performs an integral approximation with the Simpson's rule. Arguments are
    as follows:( identical to trapz )

    f          -- The function (callable) to integrate. It will be called
                  with one argument.
    N          -- Number of points to use for integration. Call "validNValues()"
                  function to find out which values of N are supported.
    xmin, xmax -- Integration interval.
    """
    if N % 2:
       raise ValueError(" You enetered N=%d, but I require that you give me an even number for N! " % N)

    # Calculate h value
    h = (xmax - xmin)/(N + eps)
    
    # Sum of first and last terms
    tot = f(xmin) + f(xmax)

    # Sum the remaining terms, where the first 'tot' are the odd terms and the second 'tot' are the even.
    for i in range(1, N, 2):
        tot += 4 * f(xmin + i * h)
    for i in range(2, N-1, 2):
        tot += 2 * f(xmin + i * h)
    # Gives back simpson integral approx
    return tot * h / 3



'''
This section initializes functions, lists and produces the result of the integration approximations for certain intervals and N values. 
'''
# functions

def f0(x):
    return np.exp(x)
def f1(x):
    return np.log(x+1)
def f2(x):
    return np.sin(2*x)**2

# lists of functions to look through
functions = [f0,f1,f2]
methods = ('Gauss Legendre Quadrature', 'Trapezoidal rule', 'Simpsons rule')
integrands = ['exp(x)', 'ln(x+1)' ,'sin(2*x)**2']

'''
A check to see if it works...

#initialize result
result = []

for f in problems:
    for method in methods:
        I = method(f, n, x0, xf)
        result.append((I, method.__name__, f.__name__, n))

# print('The functions being integrated (f0, f1 and f2) are listed here: ', integrands, '\n' )

# print ("The integral approximations are in the form(value, method, function, n value): \n",result )

'''



'''
This section will plot the relative error of each integration method used in the previous section.
'''
# x axis, M values for glq and N values for the rest
#N = np.logspace(-14,-1)
N = glq.validNValues()

# y axis, relative error as a function of N -- built inside for loop

# initialize error arrays
FN0=[]
FN1=[]
FN2=[]

# exact values for each integrand
EX0=[np.exp(2*np.pi)-np.exp(0)]
EX1=[(2*np.pi + 1)*np.log(2*np.pi + 1) - (2*np.pi)]
EX2=[np.pi]

# range of interval which integral is taken over
x0= 0
xf= 2*np.pi

# find trapz and simpsons error and give it to coloumns of FN
for n in range(len(N)):
    
    # integral approximations
    AP0 = [glq.integrate(f0, N[n], x0, xf)]
    AP1 = [trapz(f0, int(N[n]), x0, xf)]
    AP2 = [simpsons(f0, int(N[n]), x0, xf)]
    
    # Compute each relative error
    error0 = [abs((a-b)/b) for a,b in zip(AP0,EX0)]
    error1 = [abs((a-b)/b) for a,b in zip(AP1,EX1)]
    error2 = [abs((a-b)/b) for a,b in zip(AP2,EX2)]

    # Fill relative error array with y axis values
    FN0.append(error0)    
    FN1.append(error1)
    FN2.append(error2)
    

ax = plt.subplot(111)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel('N')
ax.set_ylabel('Relative error')
ax.plot(N,FN0,label=methods[0])
ax.plot(N,FN1,label=methods[1])
ax.plot(N,FN2,label=methods[2])
ax.set_title('Integration rule errors for '+ integrands[0])
ax.legend(loc= 'best')

plt.show()

