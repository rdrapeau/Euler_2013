'''
Created on Mar 5, 2013

@author: RDrapeau

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
index = 10001

# Returns the ith prime number
def ith_prime(max):
    list = [2]
    current = 3
    while len(list) < max:
        divisible = True
        for prime in list: # Check to see if it is divisible by the past prime numbers
            if current % prime == 0:
                divisible = False
        if divisible:
            list.append(current)
        current += 2 # Only prime that is even is 2
    return list.pop() # Return the maxth element

print ith_prime(index)