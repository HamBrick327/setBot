import itertools
import random

### why is the game logic harder than the computer vision

## remove random three cards from the table to test discard
def discardCards(card1, card2, card3):
    for i in range(3):
        card = random.choice(table)
        print("removing", card)
        table.remove(card)
        discard.append(card)

''' thanks aloverso, very cool '''
def is_set(card1, card2, card3) -> bool: ## was broken this whole time, now works
    ''' params: card1, card2, card3 tuples that have the attributes of SET cards (num, shading, color, shape)'''
    passes = 0
    for i in range(4):
        ## get ith attribute
        attr1 = card1[i]
        attr2 = card2[i]
        attr3 = card3[i]
        # print(attr1, attr2, attr3)
        if attr1 == attr2 and attr2 == attr3:
            passes += 1
        elif (attr1 != attr2) and (attr2 != attr3) and (attr3 != attr1):
            passes += 1
        else: ## if this condition is true ever, definitivley not a set
            # print("not a set")
            return False
    if passes == 4:
        return True

def find_sets(cards: list) -> list:
    ## takes [num, shading, color, shape]
    ''' params: cards <-- list containing cards to be plugged into is_set() '''
    sets_found = []
    i, j, k = 0
    while i < len(cards):
        j = i + 1
        while j < len(cards):
            k = j + 1
            while k < len(cards):
                if cards[i] == cards[j] or cards[j] == cards[k] or cards[i] == cards[k]: ## probably useless but I don't trust removing it
                    cards.pop(k)
                    cards.pop(j)
                    cards.pop(i)
                    continue
                if is_set (cards[i], cards[j], cards[k]):
                    sets_found.append((cards[i], cards[j], cards[k]))
                    cards.pop(k)
                    cards.pop(j)
                    cards.pop(i)
                k += 1
            j += 1
        i += 1

    return sets_found
''' end stolen code (ish) '''

num = [1, 2, 3]
shading = ["hollow", "striped", "full"]
color = ["red", "purple", "green"]
shape = ["bean", "oval", "diamond"]

def getDeck():
    ## works, generates all possible cards
    cards = list(itertools.product(num, shading, color, shape))
    for card in cards:
        card = list(card)
        for i in card:
            if type(i) == str:
                if i == "bean" or i == "oval" or i == "diamond":
                    i, card[1] = card[1], i
                elif i == "hollow" or i == "striped" or i == "solid":
                    i, card[2] = card[2], i
                elif i == "red" or i == "purple" or i == "green":
                    i, card[3] = card[3], i
    
    return cards

deck = getDeck()
cards = deck
table = []
discard = []

## add the random cards to the table and remove them from the deck
for i in range(12):
    card = random.choice(deck)
    table.append(card)
    deck.remove(card)

## display results
print(str(table).replace("),", "\n"))
sets = find_sets(table)
print(len(sets))
print(str(sets).replace("),", "\n"))
