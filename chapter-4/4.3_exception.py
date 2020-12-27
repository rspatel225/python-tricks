class CardValidationError(ValueError):
    pass

class IncorrectRankError(CardValidationError):
    pass

class IncorrectSuitError(CardValidationError):
    pass

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

card = Card(15, 'spades')

def validate(card):
    if card.suit not in ['spades', 'diamonds', 'clubs', 'hearts']:
        raise IncorrectSuitError(card.suit)
    elif not 1 <= card.rank <= 13:
        raise IncorrectRankError(card.rank)

try:
    validate(card)
except CardValidationError as err:
    # err is the card rank or suit not the error class
    print('something went wrong')