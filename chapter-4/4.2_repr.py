class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return f'{self.__class__.__name__}' f'({self.rank!r}, {self.suit!r})'

    def __str__(self):
        return f'{self.rank} of {self.suit}s'

card = Card(4, 'Spade')
print(str(card))
print(repr(card))

    