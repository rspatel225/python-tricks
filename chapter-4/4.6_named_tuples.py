from collections import namedtuple

Card = namedtuple('Card', [
    'rank',
    'suit',
])

my_card = Card(7, 'Spades')
print(my_card.rank)
print(my_card.suit)

PowerCard = namedtuple('PowerCard', Card._fields + ('power',))

power_card = PowerCard(8, 'Hearts', 'Next player draws two cards.')
print(power_card.power)