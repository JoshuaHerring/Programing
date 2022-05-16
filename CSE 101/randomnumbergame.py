import random

play = True

while play == True:
    number = random.randint(1,100)
    tries = 0
    again = False
    guess = -1
    while guess != number:
        guess = int(input('Guess'))
        if guess > number:
            print('Too High')
        if guess < number:
            print('Too low')
        if guess == number:
            print(f'Congragulations you got the magic number in {tries} tries!')
        tries = tries + 1
    play = input('WOuld you like to play agian? yes/no: ')
    if play == ('yes'):
        play = True
    elif play==('no'):
        play=False