'''
Created on Mar 13, 2013

@author: RDrapeau

In England the currency is made up of pound, E, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
It is possible to make E2 in the following way:

1xE1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can E2 be made using any number of coins?
'''

coins = [1, 2, 5, 10, 20, 50, 100, 200] # All possible coin values

def make_change(amount, index, coins):
    if index == len(coins) - 1:
        return 1
    total = 0
    taken = coins[index] * 0
    while taken <= amount:
        
        total += make_change(amount - taken, index + 1, coins)
        if not index == len(coins) - 1:
            taken += coins[index]
    return total
    

print make_change(200, 0, coins)