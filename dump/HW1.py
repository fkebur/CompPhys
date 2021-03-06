#!/usr/bin/python

# Objective: read co-ordinates, plot points, print # of points, allow for STDIN
# Make code flexible ~ specifically for #'s sep by commas, whitespace etc

import numpy as np
import matplotlib.pyplot as plt

# Specify input file by command line
inputFile = input('\n' + 'Hi, please enter your x,y dataset filename for plotting: ')

# Print the number of points
x = []
y = []

with open(inputFile) as f:
    
    lines = f.readlines()
    
    for line in lines:
       
        a = line.strip()
        
        if a.startswith('#'):
            continue
        
        if len(a) == 0:
            continue
        
        ttable = str.maketrans(',',' ')
        b = a.translate(ttable).split()
        
        x.append(float(b[0]))
        y.append(float(b[1]))
plt.scatter(x, y)
plt.show()
