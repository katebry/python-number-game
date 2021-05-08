import random

guesses = 0

print('Hello, what is your name?')
myName = input()
print('Hi ' + myName +
      ' nice to meet you, let\'s play a game. I\'m thinking of a number between 1 and 20...')

number = random.randint(1, 20)

for i in range(5):
    print('Guess the number')
    guess = input()
    guess = int(guess)
    guesses = guesses + 1

    if guess < number:
        print('Your guess is too low...')
    if guess > number:
        print('Your guess is too high...')
    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print('Good job ' + myName +
          '! You guessed my number in ' + guesses + ' guesses!')
