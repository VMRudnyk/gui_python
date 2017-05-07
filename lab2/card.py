class Card(object):
    def __init__(self, rank, suit, isVisible = False):
        self.rank = rank
        self.suit = suit
        self.isVisible = isVisible

    def __str__(self):
        return str(self.rank) + " " + str(self.suit)

    def get_rank(self):
           return self.rank