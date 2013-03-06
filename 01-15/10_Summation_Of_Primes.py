'''
Created on Mar 5, 2013

@author: RDrapeau

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math

max = 2000000

# Returns the sum of primes below max 
def sum_primes(max):
    primes = 0
    if max > 2:
        primes = 2
    number = 3
    while number < max:
        if is_prime2(number):
            primes += number
        number += 2
        print number
    return primes

# Returns whether or not n is prime
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

print sum_primes(max)