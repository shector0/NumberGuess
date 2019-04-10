# This is a guess the number game

import random

print("Hello, What is your name? ")
name = input()
print("Well " + name +", I am thinking of a number between 1 and 20")

SecretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
	print("Take a guess.")
	guess = int(input())

	if guess < SecretNumber:
		print("Your guess is too low.")
	elif guess > SecretNumber:
		print("Your guess is too high.")
	else: break #THis condition is for a correct guess


if guess == SecretNumber:
	print("Good job, " + name + "! You guessed my number in " + str(guessTaken) + " guesses.")
else:
	print("Nope. The number I was thinking of was " + str(SecretNumber))

