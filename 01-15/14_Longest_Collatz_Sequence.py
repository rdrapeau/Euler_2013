'''
Created on Mar 6, 2013

@author: RDrapeau

The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
input = 1000000

sequence = {}

# Returns the starting number up to max that produces the longest chain of Collatz numbers
def longest_sequence(max):
    longest_chain = 0
    starting_number = 0
    for i in range(1, max):
        n = get_next(i)
        list = [n]
        while n != 1:
            n = get_next(n)
            list.append(n)
        if len(list) > longest_chain:
            longest_chain = len(list)
            starting_number = i
    return starting_number

# Returns the next number in the Collatz sequence
def get_next(n):
    if n in sequence:
        return sequence[n]
    elif n % 2 == 0:
        sequence[n] = n / 2
    else:
        sequence[n] = 3 * n + 1
    return sequence[n]
    
print longest_sequence(input)