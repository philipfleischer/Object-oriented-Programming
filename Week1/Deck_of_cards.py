import random

def make_card_deck() -> list:
    """
    A function to create a deck of cards, with numbers and suits.
    Returns a list of cards. 
    """
    deck = []
    for value in range(1,14):
        for suit in ("H", "S", "D", "C"):
            deck.append((value, suit))
    return deck

def shuffle_deck(deck: list) -> list:
    """
    A function to shuffle a deck of cards. Needs a deck of cards as input. 
    Return a list of 13 shuffled cards for the holder, using pop().
    """
    random.shuffle(deck)
    deck_hand = [deck.pop() for _ in range(13)]
    return deck_hand

def sort_deck(deck_hand: list) -> list:
    """
    A function to sort a deck of cards. Needs a deck of cards list as input.
    Returns a sorted deck of cards.
    """
    deck_hand.sort()
    deck_hand.sort(key=lambda e: e[1])
    return deck_hand

def print_deck(deck: list):
    """
    A function to print every element in the deck of cards. 
    Needs a list as input.
    """
    for card in deck:
        print(card)

def main():
    deck = make_card_deck()
    shuffled_deck = shuffle_deck(deck)
    sorted_deck = sort_deck(shuffled_deck)
    print_deck(sorted_deck)

main()