class Car:
    # class variable
    count = 0

    def __init__(self, name):
        self.__class__.count += 1
        # instance variable
        self.name = name
    
audi = Car('audi')
bmw = Car('bmw')

print(f'{Car.count = }')
print(f'{audi.__class__.count = }')

