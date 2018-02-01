# Computational Physics - Lab 1
# Part 2 -- QSolve module
# Kebur Fantahun

import numpy as np

def QSolve_Cancel(a,b,c):
	
	# Initialize variables for future solutions x1 and x2
	# and the discriminant

	d = b*b - 4*a*c
	x1 = (-b+d**0.5)/(2*a) 
	x2 = (-b-d**0.5)/(2*a) 
	ZeRoot = -b/(2*a)

	# Calculate roots; all cases

	if d < 0:
		print('No real roots.')
	elif d == 0:
		print('The standard algorithm root is ',ZeRoot )
	else: 
		if x1 != x2:
			print('The standard algorithms roots are ',x1 , ' and ', x2)
			return x1,x2
		elif x1 == x2:
			print('The standard algorithm root is ', x1)
			return x1

def QSolve_NoCancel(a,b,c):
	
	# Calculate the discriminant

	d = b*b - 4*a*c
	
	# Initialize variables for future solutions x3 and x4

	x3 = (-b-np.sign(b)*d**0.5)/(2*a) 
	x4 = c/(a*x3) 
	ZeRoot = -b/(2*a)
	
	# Calculate roots
	
	if b == 0:
		print('You just killed puppies trying to divide by 0! Pick another 2nd value next time, you animal.' )
	else:
		if d < 0:
			print('No real roots.')
		elif d == 0:
			print('The improved algorithm root is ',ZeRoot )
		else: 
			if x3 != x4:
				print('Roots are ',x3 , ' and ', x4,' for the imporved algorithm.')
				return x3, x4	
			elif x3 == x4:
				print('Root is ', x3,' for the impoved algorithm.')
				return x3

