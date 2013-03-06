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
        if is_prime(number):
            primes += number
        number += 2
    return primes

# Returns whether or not n is prime
def is_prime(n):
    return is_prime_helper(2, n, n) == 1

def is_prime_helper(a, exp, n):
    if exp == 0:
        return 1
    elif exp % 2:
        number = is_prime_helper(a, exp / 2, n)
        return number ** 2 % n
    else:
        return a * is_prime_helper(a, exp - 1, n)

print sum_primes(max)