'''
Created on Mar 5, 2013

@author: RDrapeau

The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the 
square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
'''

# Returns the square of the sum of the first max (inclusive) natural numbers
def sum_squared(max):
    sum = 0
    for n in range(1, max + 1):
        sum += n
    return sum ** 2

# Returns the sum of the squares of the first max (inclusive) natural numbers
def squares_sum(max):
    sum = 0
    for n in range(1, max + 1):
        sum += n ** 2
    return sum

print sum_squared(100) - squares_sum(100)
