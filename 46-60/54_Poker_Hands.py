'''
Created on Apr 14, 2013

@author: RDrapeau

http://projecteuler.net/problem=54
'''



f = open("poker.txt")

nDict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def checkFlush(hand):
    firstCardSuit = hand[0][1]
    for a in range(1,5):
        if hand[a][1] != firstCardSuit:
            return False
    return True

def sortedHand(hand):
    temp = []
    for a in hand:
        temp.append(nDict[a[0]])
    temp.sort()
    temp.reverse()
    return temp

def checkStraight(sortedHand):
    if sortedHand == [14, 5, 4, 3, 2]:
        return True
    for i in range(1,5):
        if sortedHand[i] != sortedHand[i-1]-1:
            return False
    return True

def checkPairs(sortedHand):
    pairs = []
    for i in sortedHand:
        if sortedHand.count(i) == 2:
            if not i in pairs:
                pairs.append(i)
    return pairs

def checkTrips(sortedHand):
    trips = []
    for i in sortedHand:
        if sortedHand.count(i) == 3:
            if not i in trips:
                trips.append(i)
    return trips

def checkQuads(sortedHand):
    quads = []
    for i in sortedHand:
        if sortedHand.count(i) == 4:
            if not i in quads:
                quads.append(i)
    return quads

def checkRank(hand):
    hSorted = sortedHand(hand)
    isFlush = checkFlush(hand)
    isStraight = checkStraight(hSorted)
    trips = checkTrips(hSorted)
    pairs = checkPairs(hSorted)
    if hSorted == [14, 13, 12, 11, 10] and isFlush:
        return ['Royal Flush', None]
    elif isStraight and isFlush:
        return ['Straight Flush', hSorted[0]]  #wheel straight???
    elif len(checkQuads(hSorted)) == 1:
        return 'Four of a Kind'
    elif len(trips) == 1 and len(pairs) == 1:
        return ['Full House', [trips[0],pairs[0]]]
    elif isFlush:
        return ['Flush', hSorted]
    elif isStraight:
        return ['Straight', hSorted]
    elif len(trips) == 1:
        return ['Three of a Kind', [trips, hSorted]]
    elif len(pairs) == 2:
        return ['Two Pairs', [pairs, hSorted]]
    elif len(pairs) == 1:
        kickers = hSorted[:]
        kickers.remove(pairs[0])
        kickers.remove(pairs[0])
        return ['One Pair', [pairs, kickers]]
    else:
        return ['High Card', hSorted]

# looks like the only ties are high card and one pair

handValue = {'Royal Flush': 10,
             'Straight Flush': 9,
             'Four of a Kind': 8,
             'Full House': 7,
             'Flush': 6,
             'Straight': 5,
             'Three of a Kind': 4,
             'Two Pairs': 3,
             'One Pair': 2,
             'High Card': 1}

p1 = 0
p2 = 0
ties = 0

for line in f:
    temp = line.replace('\n', '')
    temp2 = temp.split(' ')
    hand1 = temp2[0:5]
    hand2 = temp2[5:]
    h1Rank = checkRank(hand1)[0]
    h2Rank = checkRank(hand2)[0]
    h1Val = handValue[h1Rank]
    h2Val = handValue[h2Rank]
    if h1Val > h2Val:
        p1 += 1
    elif h1Val < h2Val:
        p2 +=1
    elif h1Val == h2Val:
        if checkRank(hand1)[1] > checkRank(hand2)[1]:
            p1 += 1
        elif checkRank(hand1)[1] < checkRank(hand2)[1]:
            p2 += 1
        else:
            ties += 1

print p1