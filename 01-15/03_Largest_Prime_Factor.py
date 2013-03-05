'''
Created on Mar 4, 2013

@author: RDrapeau

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

number = 600851475143

# Returns all the factors of a number n
def factors(n):
    max = n ** 0.5 # upper limit to search for factors
    factors_of_n = [1, n] # 1 and n are always factors 
    number = 2
    while number < max:
        if n % number == 0:
            factors_of_n.append(number)
            factors_of_n.append(n / number)
        number += 1
    factors_of_n.sort()
    return factors_of_n

# Returns the prime factors of n
def get_prime_factors(n):
    prime_factors = []
    factors_of_n = factors(n)
    for number in factors_of_n:
        if is_prime(number):
            prime_factors.append(number)
    return prime_factors

# Returns whether or not a number is prime using Fermat's Little Theorem: (a ^ (n - 1)) % n = 1
def is_prime(n):
    number = pow(120, n - 1, n) % n
    return number == 1

# Raises a base to the exp power while constantly modding by n
def pow(base, exp, n):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        number = pow(base, exp / 2, n)
        return number * number % n
    else:
        return base * pow(base, exp - 1, n) % n

print get_prime_factors(600851475143).pop()