name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'John':
        break # jumps to next line
print('Thank You!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # jumps back to start of loop
    print('spam is' + str(spam))
