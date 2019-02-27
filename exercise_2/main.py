import random

print('-----------------------------')
print('guess that number game')
print('-----------------------------')
print('')

that_number = random.randint(0, 50)
guess = -1
name = input("What's your name darling? ")

while guess != that_number:
    guess_text = input('Guess number between 0 an 50: ')
    guess = int(guess_text)

    if guess < that_number:
        print('{0}Your guess of {1} was too low. Keep trying!'.format(name, guess))

    elif guess > that_number:
        print('{0}Your guess of {1} was too big. Keep trying!'.format(name, guess))


    else:
        print('Huge congrats {0}! {1} was that number!'.format(name, guess))


print('')
print('done. thanks ;)')








