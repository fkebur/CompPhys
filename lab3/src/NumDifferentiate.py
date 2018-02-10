'''
Kebur Fantahun
Computational Physics - Lab 3 Part 1
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

def fn(x):
	''' Define function of interest '''
	return np.e**x

def ForwDiff(fn, x, h): 
	''' Take the first derivative using forawrd difference formula '''
	return (fn(x+h)-fn(x))/(h)

def SymmDiff(fn, x, h):
	''' Take the first derivative using symmetric difference formula '''
	return (fn(x+h)-fn(x-h))/(2h) 

def SymmNewH(fn, x, h):
	''' Take the first derivative using symmetric difference formula with new and imporved h '''
	x1 = x + h
	x2 = x - h
	twoh = x1 - x2 # Make h exactly representable
	return (fn(x+h)-fn(x-h))/(twoh)

def SecoDiff(fn, x, h):
	''' Take the second derivative using the three-point formula
	    Write it in this form to reduce subtractive cancellation '''

	fDblPrime = ((fn(x + h) - fn(x)) + (fn(x - h) - fn(x)))/h**2)
	return fDblPrime
