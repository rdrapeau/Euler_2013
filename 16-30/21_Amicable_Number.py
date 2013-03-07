'''
Created on Mar 7, 2013

@author: RDrapeau

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

max = 10000

# Returns whether a number is amicable or not
def is_amicable(n):
    sum_divisors = sum_factors(n)
    return n != sum_divisors and n == sum_factors(sum_divisors)
    
# Returns the sum of the factors of a number n
def sum_factors(n):
    list = factor(n)
    sum = 0
    for i in list:
        sum += i
    return sum

# Returns a list of factors of n (does not include n)
def factor(n):
    factors = []
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            if (n / x < n):
                factors.append(n / x)
    factors = list(set(factors))
    return factors

sum = 0
for x in range(1, max):
    if is_amicable(x):
        sum += x
print sum