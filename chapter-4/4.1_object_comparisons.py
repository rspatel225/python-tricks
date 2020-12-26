def greetings():
    print('Good morning')

hello = greetings
hi = greetings

print(hello == hi)
print(hello is hi)