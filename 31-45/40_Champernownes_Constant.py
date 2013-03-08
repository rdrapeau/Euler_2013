'''
Created on Mar 7, 2013

@author: RDrapeau

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''
max = 1000000

# Returns the result of multiplying together digits in champernowne's number from 1...10...100...max
def result(max, number):
    max = len(str(max))
    power = 1
    answer = 1
    for x in range(max):
        answer *= int(number[power])
        power *= 10
    return answer

# Returns a champernowne number of length max_length
def get_number(max_length):
    number = "."
    counter = 1
    while len(number) <= max_length:
        number += str(counter)
        counter += 1
    return number

number = get_number(max)
print result(max, number)
        