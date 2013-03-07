'''
Created on Mar 7, 2013

@author: RDrapeau

n! means n x (n - 1)  ...  3 x 2 x 1

For example, 10! = 10 x 9  ...  3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

# Returns the sum of the digits in n
def sum_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

# Returns the factorial of a number n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print sum_digits(factorial(100))