from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'bark'

class Cat(Animal):
    def speak(self):
        return 'meow'
    
    def eat(self):
        return 'mice'

# Can not instantiate the base class
# a = Animal()

# Can not instatiate Dog because it does not implement all base class methods
# d = Dog()

c = Cat()
print(c.speak())