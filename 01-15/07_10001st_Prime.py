'''
Created on Mar 5, 2013

@author: RDrapeau

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def is_prime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if not n % i:
            return False
    return True

def prime_list(n):
    primes = [2, 3, 5, 7, 11, 13]
    i = max(primes) + 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes

print max(prime_list(10001))
