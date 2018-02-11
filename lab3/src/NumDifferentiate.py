'''
Kebur Fantahun
Computational Physics - Lab 3 Part 1
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

def fn(x):
	''' Define function of interest '''
	return np.exp(x)
def Der(x):
	''' Exact derivative of the function of interest '''
	return np.exp(x)

def FDiff(x, h): 
	''' Take the first derivative using forawrd difference formula '''
	return (fn(x+h)-fn(x))/(h)

def SyDiff(x, h):
	''' Take the first derivative using symmetric difference formula '''
	return (fn(x+h)-fn(x-h))/(2*h) 

def SyDiffNewH(x, h):
	''' Take the first derivative using symmetric difference formula with new and imporved h '''
	x1 = x + h
	x2 = x - h
	twoh = x1 - x2 # Make h exactly representable
	return (fn(x+h)-fn(x-h))/(twoh)

def SecoDiff(x, h):
	''' Take the second derivative using the three-point formula
	    Write it in this form to reduce subtractive cancellation '''
	return ((fn(x + h) - fn(x)) + (fn(x - h) - fn(x)))/(h**2)

# Build axes for the plot
hrange = np.arange(10*sys.float_info.epsilon, 0.1, 1e-3)


# Set up and plot median relative error 
x = np.linspace(0, 2*np.pi, 100)
MRE1 =[]
MRE2 =[]
MRE3 =[]
MRE4 =[]


for h in hrange:
	
	# Compute each derivative
	f_ex  = fn(x)
	ffor  = FDiff(x,h)
	fsym1 = SyDiff(x,h)
	fsym2 = SyDiffNewH(x,h)
	fsec  = SecoDiff(x,h)

	# Compute each relative error
	error1 = [abs(1-a/b) for a,b in zip(ffor,f_ex)]
	error2 = [abs(1-a/b) for a,b in zip(fsym1,f_ex)]
	error3 = [abs(1-a/b) for a,b in zip(fsym2,f_ex)]
	error4 = [abs(1-a/b) for a,b in zip(fsec,f_ex)]
	
	# Find the median of the above errors
	med1 = np.median(error1)
	med2 = np.median(error2)
	med3 = np.median(error3)
	med4 = np.median(error4)
	
	# Fill median arry for y axix values
	MRE1.append(med1)	
	MRE2.append(med2)	
	MRE3.append(med3)	
	MRE4.append(med4)

ax = plt.subplot(111)
ax.set_xscale("log")
ax.set_yscale("log")
ax.plot(hrange,MRE1,label="Forward difference first derivative")
ax.plot(hrange,MRE2,label="Symmetric difference first derivative")
ax.plot(hrange,MRE3,label="Symmetric(new h) difference first derivative")
ax.plot(hrange,MRE4,label="Three point second derivative")
ax.set_title('Mean relative error(as a function of h) vs h')
ax.legend(loc= 'upper right')
ax.grid(True)
min1 = np.argmin(MRE1)
print(min1)
plt.show()
