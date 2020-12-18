import functools

def intials(func):
    # helps maintain the original function's name and docs
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'name' in kwargs:
            for word in kwargs['name'].split():
                print(word[0], end='.')
            print()
            func(*args, **kwargs)
    return wrapper

@intials
def player(name):
    """Prints a players name."""
    print(name)

player(name='Derrick Rose')
print(player.__name__)
print(player.__doc__)

