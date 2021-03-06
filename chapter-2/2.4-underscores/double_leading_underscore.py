_Honda__turbo = True

class Automobile:
    def __init__(self):
        # property is named _Automobile__legal
        self.__legal = True
        self.gears = 6
    
class Honda(Automobile):
    def __init__(self):
        super().__init__()
        self.gears = 4
        self._manual = True
    
    def getTurbo(self):
        # gets mangled into _Honda__turbo which is the same name as the global variable
        return __turbo

a = Automobile()
h = Honda()

print('automobile:', dir(a), '\n')
print('honda:', dir(h), '\n')
# the legal variable still exist in the sub class as _Automobile__legal
print(f'{h._Automobile__legal = }')
print(f'{h.getTurbo() = }')