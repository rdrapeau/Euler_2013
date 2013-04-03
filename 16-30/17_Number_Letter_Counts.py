'''
Created on Mar 10, 2013

@author: RDrapeau

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing 
out numbers is in compliance with British usage.
'''
lengths = {}

lengths[1] = 3
lengths[1] = 3
lengths[2] = 3
lengths[3] = 5
lengths[4] = 4
lengths[5] = 4
lengths[6] = 3
lengths[7] = 5
lengths[8] = 5
lengths[9] = 4
lengths[10] = 3
lengths[11] = 6
lengths[12] = 6
lengths[13] = 8
lengths[14] = 8
lengths[15] = 7
lengths[16] = 7
lengths[17] = 9
lengths[18] = 8
lengths[19] = 8
lengths[20] = 6
lengths[30] = 6
lengths[40] = 5
lengths[50] = 5
lengths[60] = 5
lengths[70] = 7
lengths[80] = 6
lengths[90] = 6
lengths[100] = 7
lengths[1000] = 11

def evaluate(n):
    top = high(n / 100 * 100)
    bottom = low(n % 100)
    result = top + bottom
    if top != 0 and bottom != 0:
        result += 3
    return result

def high(n):
    if n == 0:
        return n
    if n == 1000:
        return lengths[n]
    return low(n / 100) + lengths[100]

def low(n):
    if n == 0:
        return 0 
    if n in lengths: 
         return lengths[n] 
    return low(n % 10) + lengths[n / 10 * 10]

sum = 0
for x in range(1, 1001):
    sum += evaluate(x)
print sum

