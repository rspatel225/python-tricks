class Dog:
    def __init__(self, name, breed, food):
        self.name = name
        self.breed = breed
        self.food = food

    def __repr__(self):
        return f'Dog({self.name!r}, {self.breed!r}, {self.food!r})'

    # instance method
    def speak(self):
        return 'bark'

    # class method, a factory function
    @classmethod
    def boxer(cls, name):
        return cls(name, ['boxer'], ['dog food'])

    # static method
    @staticmethod
    def number_of_legs():
        return 4


clifford = Dog('Clifford', 'big red dog', 'dog treats')
print(f'{clifford.speak() = }')
print(f'{Dog.boxer("Spike") = }')
print(f'{Dog.number_of_legs() = }')

