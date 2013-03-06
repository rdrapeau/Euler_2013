'''
Created on Mar 5, 2013

@author: RDrapeau

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
# Returns 3 numbers multiplied together which represent a Pythagorean Triplet
def get_triplet(max):
    product = -1
    for a in range(1, max - 2): # Must add up to max
        for b in range(1, max - a):
            c = max - a - b
            if is_pyth_triple(a, b, c):
                product = a * b * c
    return product

# Returns whether or not the numbers a,b,c are Pythagorean Triplets
def is_pyth_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

print get_triplet(1000)
