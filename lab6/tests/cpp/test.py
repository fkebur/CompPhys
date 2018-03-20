from numpy import *
import pylab as p
from mpl_toolkits.mplot3d import Axes3D

print( "Initializing" )
 
# maybe Float instead?
Nmax = 100; Niter = 70; V = zeros ((Nmax, Nmax) , float )

print("Working hard, wait for the figure while I count to 60")

# line at 100 V
for k in range(0, 99):
    V[0,k] = 100.0

for iter in range(Niter):

    if iter%10 == 0: print(iter)
    
    for i in range (1 , 98):
        for j in range(1, 98):
            V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

x = range(0, 99, 2)
y = range(0, 50, 2)

X, Y = p.meshgrid(x,y)

def functz(V):
    z = V[X,Y]
    return z


Z = functz(V) 
fig = p.figure() # create figure
ax = fig.add_subplot(111, projection='3d') # plot axes
ax.plot_wireframe(X, Y, Z,color = 'k') # red wirefram
ax.set_xlabel('X') # label axes
ax.set_ylabel('Y')
ax.set_zlabel('Potential')

# display fig, Ctrl C to quit
p.show()
