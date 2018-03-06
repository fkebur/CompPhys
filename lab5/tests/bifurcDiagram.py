#!/usr/bin/python

from AngleValue import *
import matplotlib.pyplot as plt
import pickle
from multiprocessing import Pool
import time
import pandas as pd

start = time.time()

F_D = np.arange(0.5,2.5,0.2)
theta0 = np.linspace(0, 1, 200)

def AngleArray(f):
    x_array = np.array([])
    for t in theta0:
        x = AngleValue(t, f)
        a_array = np.hstack((x_array,x))     
    return a_array

cores = Pool(4)
data = cores.map(AngleArray, F_D)
fullX = np.ravel(data)

domain = np.zeros(len(fullX))
for i in range(len(F_D)):
    # number of F_D "sections"
    n = int(len(fullX)/len(F_D))
    # fill each F_D sections with its respective angle
    domain[i*n:(i+1)*n] = F_D[i]

df = pd.DataFrame({'x':domain, 'y':fullX})
ddupl = df.drop_duplicates()
X = np.asarray(ddupl['x'])
Y = np.asarray(ddupl['y'])

plt.figure(figsize=(80,80))

SMALL_SIZE = 50
MEDIUM_SIZE = 80
BIGGER_SIZE = 120
plt.rc('axes', titlesize=BIGGER_SIZE)
plt.rc('axes', labelsize=MEDIUM_SIZE)    
plt.rc('xtick', labelsize=SMALL_SIZE)    
plt.rc('ytick', labelsize=SMALL_SIZE)    
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.plot(X,Y,'c')
plt.title("Bifurcation")
plt.xlabel("F_D")
plt.ylabel("Angles")
plt.savefig('bifurcDiagram.pdf', format='pdf')
plt.close()

end = time.time()

print(end - start)
