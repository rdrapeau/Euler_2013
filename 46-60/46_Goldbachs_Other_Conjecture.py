'''
Created on Apr 14, 2013

@author: RDrapeau

It was proposed by Christian Goldbach that every odd composite number can be written as 
the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True
 
def isPerfectSquare(n):
    if n < 0:
        return False
    result = int(n**0.5)
    return result * result == n
 
odd = 9
flag = True
while flag:
    if isPrime(odd): 
        odd += 2
    oddPass = False
    for i in range(2,odd-1):
        if isPrime(odd - i) and i % 2 == 0 and isPerfectSquare(i / 2):
            oddPass = True
            break
    if oddPass:
        odd += 2
    else:
        print odd
        flag = False
