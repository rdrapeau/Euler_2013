'''
Created on Mar 5, 2013

@author: RDrapeau

The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math
target = 500

# Returns the first triangle number to have over target divisors
def triangle_nums(target):
    factors = [1]
    previous = 1
    counter = 2
    while len(factors) < target:
        factors = []
        previous = counter + previous
        factors = factor(previous)
        counter += 1
    return previous
       
# Returns a list representing the factors of n 
def factor(n):
    factors = [n]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)
    return list(set(factors))
        
print triangle_nums(target)
