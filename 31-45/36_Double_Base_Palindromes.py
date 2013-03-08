'''
Created on Mar 7, 2013

@author: RDrapeau

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

max = 1000000

# Returns the sum of all number less than max that are palindromic in base 10 and base 2
def find_sum(max):
    sum = 0
    for n in range(max):
        if is_palindrome(n) and is_palindrome(to_binary(n)):
            sum += n
    return sum

# Returns whether or not a number is a palindrome or not
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Returns the number n in base 2
def to_binary(n):
    return int(bin(n)[2:])

print find_sum(max)