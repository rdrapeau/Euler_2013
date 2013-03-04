'''
Created on Mar 4, 2013

@author: RDrapeau

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Returns the possible numbers that are divisible by 3 or 5 below max
def possible_nums(max):
    list = []
    for n in range(max):
        if n % 3 == 0 or n % 5 == 0:
            list.append(n)
    return list

# Returns the sum of the list
def get_sum(list):
    sum = 0
    for n in list:
         sum += n
    return sum

list = possible_nums(1000)
print get_sum(list)