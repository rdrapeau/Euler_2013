'''
Created on Mar 10, 2013

@author: RDrapeau

The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and 
adding these values we form a word value. For example, the word value for 
SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
'''

# Gets the nth triangle number
def get_triangles(n):
    triangles = []
    for i in range(1, n + 1):
        triangles.append(0.5 * i * (i + 1))
    return triangles 

# Returns the sum of the indexs of a word
def get_sum(word):
    sum = 0
    for letter in word:
        sum += get_ASCII_value(letter)
    return sum

# Returns the index of the input char in the alphabet
def get_ASCII_value(char):
    return ord(char) - 64

# Gets all the words from a txt file to consider
def get_data():
    file = open("words.txt", 'r')
    return str(file.readline()).replace('"', "").split(",")

words = get_data()
triangles = get_triangles(20)
count = 0
for word in words:
    if get_sum(word) in triangles:
        count += 1
print count