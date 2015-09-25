# This is a guess the number game about codeX student.
import random

guessesTaken = 0

print('Hello! Please tell me your name! now!!')
myName = input()#This where you insert an input(use the Terminal)

number = random.randint(20, 30)
print(myName + ", Wow! That's a Cool name")
print("How many students we have here at CodeX?")
print("Please guess a number between 20 and 30")
while guessesTaken < 4:
    print('Take a guess,Please!') # There are four spaces in front of print.
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
    print('Awesome!, ' + myName + '! You guessed CodeX students in ' + guessesTaken + ' guesses!')

#if guess != number:
elif guess != number:
     number = str(number)
     print('Uyaxoka(Xhosa). The number I was thinking of was ' + number)

else:
    print("You are idiot!")