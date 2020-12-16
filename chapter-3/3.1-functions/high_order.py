def mixture(flavor):
    if flavor == 'orange':
        print('Crush')
    elif flavor in ['lime', 'lemon']:
        print('Sprite')
    else:
        print('Cola')


def drink(func):
    func('orange')


if __name__ == '__main__':
    drink(mixture)