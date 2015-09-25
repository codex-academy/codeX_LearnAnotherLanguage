# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! Please tell me your name! now!!')
myName = input()

number = random.randint(3, 5)
print(myName + ', Wow! That\s a Cool name')
print("How many terms of study we have here at CodeX?")
print("Please guess a number between 3 and 5")
while guessesTaken < 4:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print(myName + ',Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print(myName + ',Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Awesome!, ' + myName + '! You guessed CodeX Terms in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)