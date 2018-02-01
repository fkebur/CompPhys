#!/usr/bin/env python
#########################################################################
#
# The program below has very little content but it can serve as
# a simple skeleton for your future scripts in case the script
# always takes the same number of arguments and you do not need
# complicated argument parsing.
#
# More complicated command line parsing patterns are discussed at
# http://code.activestate.com/recipes/278844/
#
# Make this script executable by running "chmod a+x hello2.py"
# at the shell prompt.
#
#########################################################################

"""
Usage: hello2.py n_times name
"""

import sys

def hello(n, who):
    for i in range(n):
        print("Hello, %s!" % who)
    return

def main(argv):
    # Parse command line options
    argc = len(argv)
    if (argc == 0):
        # Convention used here: command invoked without any arguments
        # prints its usage instruction and exits successfully
        print(__doc__)
        return 0
    elif (argc == 2):
        # We have the correct number of arguments
        i = 0
        ntimes = int(argv[i]); i+=1
        name = argv[i]; i+=1
    else:
        # The number of arguments is incorrect
        print(__doc__)
        return 1
    # Call the code which does the job
    hello(ntimes, name)
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))
