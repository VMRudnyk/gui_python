from card import Card


class Pyramid(object):
    def __init__(self):
        self.deck_pyramid = []

    def right(self, card_numb, row):
        return card_numb + 1 - row

    def left(self, card_num, row):
        return card_num - row

    def call(self, card_numb):
        summa = 0
        row = 0

        while summa < card_numb:
            summa += row + 1
            row += 1
        print(summa)
        if card_numb == summa:
            print('This is right edge card')
            return [self.right(card_numb, row)]
        elif card_numb == summa + 1 - row:
            print('This is left edge card')
            return [self.left(card_numb, row)]
        else:
            print('This is middle card')
            return [self.left(card_numb, row), self.right(card_numb, row)]

    def add(self, card: Card):
        if len(self.deck_pyramid) > 21:
            card.isVisible = True
        elif len(self.deck_pyramid) > 28:
            raise StopIteration
        self.deck_pyramid.append(card)