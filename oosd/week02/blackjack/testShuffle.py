__author__ = 'mazurdm1'
import deck
import math
import card

distrubution = [0] * 52
card_deck = deck.Deck()

for i in range(0, 520):
    card_deck.shuffle(0)
    distrubution[card_deck.cards.index()] += 1


print(min(distrubution))