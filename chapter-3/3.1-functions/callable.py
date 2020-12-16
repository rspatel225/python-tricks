class Multiply():
    def __init__(self, num):
        self.num = num
    
    def __call__(self, x):
        return self.num * x

if __name__ == "__main__":
    by3 = Multiply(3)
    print(callable(by3))
    print(by3(20))