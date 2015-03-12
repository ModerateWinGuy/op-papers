import card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle_kinds = [shuffle_one, shuffle_two, shuffle_three]
        
        for suit in "CDHS":
            for val in range(1, 11):
                self.cards.append(card.Card(val, suit))
            for val in "AKQJ":
                self.cards.append(card.Card(val, suit))
        self.random.choice(self.shuffle_kinds)(self.cards)

    def next(self):
        return self.cards.pop()
        

def shuffle_one(deck):
    random.shuffle(deck)


def shuffle_two(deck):
    for i in deck:
        swap(i, random.randint(0, len(deck)))


def shuffle_three(deck):
    shuffle_one(deck)
    shuffle_two(deck)


def swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp