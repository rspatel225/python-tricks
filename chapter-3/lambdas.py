mult = lambda x, y: x * y
cards = [
    (1, 's'),
    (10, 'c'),
    (12, 'h'),
]

if __name__ == "__main__":
    print(mult(10, 5))
    print((lambda string: string.upper())('hello, world'))
    print(sorted(cards, key=lambda card: card[1]))