import itertools
import random

''' WORKS 5/19/24 '''

num = [1, 2, 3]
shading = ["hollow", "striped", "full"]
color = ["red", "purple", "green"]
shape = ["bean", "oval", "diamond"]

## works, generates all possible cards
cards = list(itertools.product(num, shading, color, shape))
cards = [set(card) for card in cards] ## whole deck
print(type(cards[1]))

deck = cards
table = []
discard = []
## add the random cards to the table and remove them from the deck
for i in range(12):
    card = random.choice(deck)
    table.append(card)
    deck.remove(card)

print(table)
print()
print()
## remove random three cards from the table to test discard
for i in range(3):
    card = random.choice(table)
    table.remove(card)
    discard.append(card)

print(discard)
print()
print(table)

def checkSet(set: table):
    pass ## use set.intersect()

    ## remove cards from the table here