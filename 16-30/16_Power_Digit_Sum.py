'''
Created on Mar 7, 2013

@author: RDrapeau

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

base = 2
exp = 1000

# Returns the sum of all the digits in n
def get_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

# Returns base raised to the exp power
def pow(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        num = pow(base, exp / 2)
        return num ** 2
    else:
        return base * pow(base, exp - 1)
    
print get_sum(pow(base, exp))