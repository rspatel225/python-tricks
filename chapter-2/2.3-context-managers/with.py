# the file closes once outside of the with block
with open('info.txt', 'w') as f:
    f.write(input('Text: '))

with open('info.txt', 'r') as f:
    print(f.read())
