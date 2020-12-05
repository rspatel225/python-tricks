from move import move

walk = move

if __name__ == '__main__':
    # the function object and the name of the function are seperate
    print(f'{walk = }')
    print(f'{move = }')
    del move
    print(f'{walk = }')
    # move does not exist error
    print(f'{move = }')
     
    