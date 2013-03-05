'''
Created on Mar 4, 2013

@author: RDrapeau

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
numbers_to_check = [11, 13, 14, 16, 17, 18, 19, 20]

# Returns the smallest number that passes check(number)
def solve():
    largest = numbers_to_check.pop()
    number = largest
    while (not is_divisible(number)):
        number += largest
    return number

# Returns whether or not n is evenly divisible by all numbers_to_check
def is_divisible(n):
    for number in numbers_to_check:
        if n % number != 0:
            return False
    return True

print solve()
