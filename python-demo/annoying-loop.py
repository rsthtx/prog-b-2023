name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


# Using a break statement
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')