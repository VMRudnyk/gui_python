from itertools import product
from random import shuffle
from card import Card


class Deck(object):
    def __init__(self):
        #ранги
        ranks = range(1, 14)
        #масти
        suits = "Diamonds", "Spades", "Clubs", "Hearts"
        #генератор списків, що створює колоду з 52 карт
        self.cards = [Card(rank, suit) for rank, suit in product(ranks, suits)]
        shuffle(self.cards)

    def deal_cards(self):
        return self.cards.pop()

    def __iter__(self):
        return self

    def __next__(self):

        if len (self.cards) == 0:
            raise StopIteration
        else:
            card = self.cards.pop()
            return card