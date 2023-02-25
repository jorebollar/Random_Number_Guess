#import random module
import random

#Random number genrator between 1 and 10
number = random.randint(1, 10)

#Ask user input between 1 and 10
guess = input("Guess a number between 1 and 10: ")

#User input string converted to an integer
guess = int(guess)

#Checking user guess
if guess == number:
    print("You guessed correctly!")
elif guess < number:
    print("You guessed low")
elif guess > number:
    print("You guessed high")

guesses = 0

while guess != number:

    print("Congrats, you guessed the number in" , guesses, "guesses!")
