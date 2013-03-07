'''
Created on Mar 7, 2013

@author: RDrapeau

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

# Returns the number of paths to get from the top left to the bottom right of a grid of size size
def fact(n):
    f = 1
    for x in xrange(1, n + 1): 
        f = f * x
    return f

print fact(40) / fact(20) / fact(20)