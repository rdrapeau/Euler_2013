'''
Created on Mar 4, 2013

@author: RDrapeau

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''

fibonacci_numbers = {} # Fibonacci numbers already calculated
fibs = [0, 1]

# Fills the array with the fibonacci numbers up until max
def fillFibs(max):
    a = fibs[0]
    b = fibs[1]
    while b < max:
        c = b
        b += a
        a = c
        fibs.append(b)

fillFibs(4000000)
sum = 0
for n in fibs:
    if n % 2 == 0:
        sum += n

print sum