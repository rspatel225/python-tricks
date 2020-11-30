# dunder methods are core to python 
class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return f'Player: {self.name}'

kobe = Player('Kobe Bryant')
print(kobe)