import copy

x = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    'one layer'
]

# a pointer to x
y = x
# a shallow copy of x
z = list(x)
# a deep copy of x
a = copy.deepcopy(x)

print(f'{y = }')
print(f'{z = }')
print(f'{a = }')

x[0][2] = 100
x[2] = 'changed'
x.append(['hello, world'])
print('Made changes to x')

print(f'{y = }')
print(f'{z = }')
print(f'{a = }')