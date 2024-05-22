from typing import List, Tuple
''' written by ChatGPT'''
# Define a card as a tuple of (number, shape, shading, color)
Card = Tuple[int, str, str, str]

def is_set(card1: Card, card2: Card, card3: Card) -> bool:
    """
    Determines if three cards form a valid set.
    
    Parameters:
    card1, card2, card3 (Card): Three cards to be checked.
    
    Returns:
    bool: True if the cards form a set, False otherwise.
    """
    for i in range(4):
        # Collect the ith attribute from all three cards
        attrs = {card1[i], card2[i], card3[i]}
        # Check if all are the same or all are different
        ''' if the length is 1, then all are the same because python sets, if the length is 3, then all are different because nothing canceled out '''
        if not (len(attrs) == 1 or len(attrs) == 3):
            return False
        else: ## can also remove the else statement and leave it after the if statement, but this is more readable
            return True

def find_sets(cards: List[Card]) -> List[Tuple[Card, Card, Card]]:
    """
    Finds all possible sets from a list of cards.
    
    Parameters:
    cards (List[Card]): List of cards to check.
    
    Returns:
    List[Tuple[Card, Card, Card]]: List of all found sets.
    """
    sets_found = []
    n = len(cards)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_set(cards[i], cards[j], cards[k]):
                    sets_found.append((cards[i], cards[j], cards[k]))
    return sets_found

# Example usage
cards = [
    (1, 'squiggle', 'striped', 'purple'),
    (2, 'diamond', 'solid', 'green'),
    (3, 'oval', 'open', 'red'),
    (1, 'diamond', 'striped', 'purple'),
    (2, 'squiggle', 'solid', 'red'),
    (3, 'diamond', 'open', 'purple'),
    (1, 'oval', 'striped', 'green'),
    (2, 'oval', 'open', 'purple'),
    (3, 'squiggle', 'solid', 'red'),
    (1, 'diamond', 'open', 'purple'),
    (2, 'oval', 'striped', 'green'),
    (3, 'diamond', 'solid', 'red')
]

sets = find_sets(cards)
print(f"Found {len(sets)} sets:")
for s in sets:
    print(s)
    print(len(cards))
