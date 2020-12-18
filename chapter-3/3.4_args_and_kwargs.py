def magic(*args, **kwargs):
    kwargs['trick'] = 'disappear'
    args = args + (33,)
    if args:
        print(f'{args = }')
    if kwargs:
        print(f'{kwargs = }')
        
magic('hello', 'there', 23, time=600, space='Milky Way', color=['blue', 'black'])