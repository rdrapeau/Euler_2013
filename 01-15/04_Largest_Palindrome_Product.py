'''
Created on Mar 4, 2013

@author: RDrapeau

A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Returns the largest palindrome made from the product of two digit-digit numbers
def largest_palindrome(digit):
    palindromes = []
    for x in range(10 ** (digit - 1), 10 ** digit):
        for y in range(x, 10 ** digit):
            n = x * y
            if is_palindrome(n):
                palindromes.append(n)
    palindromes.sort()
    return palindromes.pop()
        
            
# Returns whether the number n is a palindromic number or not
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print largest_palindrome(3)

