# Computational Physics - Lab 1
# Part 2 -- executable for qsolve module
# Kebur Fantahun

import qsolve 

a, b, c = map(float, input('Please enter 3 numbers that build a quadratic equation to solve: (add a space between each #) ').split())
print('\n'+ 'This program will demonstrate the difference in quadratic root algorithms.'
' The classic form of a quadratic equation is: a*x**2 + b*x +c .'
'\n' + 'Here I`ve decided to use a = 1, b = 200, and c =1 in order to get a root near 0.'
'\nTo vary a, b and c, one should go into the program and uncomment line 7. '
'Another good example is shown when a = 1, b = 200 and c = -0.00010.\n')

#a = 1
#b = 200
#c = 1


# The canonical quadratic root solver, prone to subtractive cancellation.
qsolve.QSolve_Cancel(a,b,c)
# The alternative quadratic solving method. Known to avoid the above problem
qsolve.QSolve_NoCancel(a,b,c)

# Compare the two solutions
print('\n', 'After comparison of the above rows of values, ' 
'it is clear that the standard algorithm does not quite ' 
'reach the correct values. The improved algorithm provides a clean '
' answer, free of subtractive cancellation.' ) 
