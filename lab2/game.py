from deck import Deck
from pyramid import Pyramid


class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.pyramid = Pyramid()
        for i in range(28):
            self.pyramid.deck_pyramid.append(self.deck.__next__())

        for card in self.pyramid.deck_pyramid:
            print(card)
        print("-----------")

g = Game()
p = Pyramid()
p.call(8)