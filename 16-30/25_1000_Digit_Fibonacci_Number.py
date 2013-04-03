'''
Created on Mar 5, 2013

@author: RDrapeau

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

dict = {} # Fibonacci numbers already calculated

# Returns the first number in the Fib sequence to contain n digits
def get_nth_digit(n):
    number = 0
    counter = 0
    while len(str(number)) < n:
        counter += 1
        number = fib(counter)
    return counter

# Returns the nth number in the Fibonacci sequence
def fib(n):
    if n in dict: # Already computed this number
        return dict[n]
    elif n < 2:
        dict[n] = n
        return n
    else:
        dict[n] = fib(n - 1) + fib(n - 2)
        return dict[n]

print get_nth_digit(1000)
print fib(4782)