#import random module
import random

#Random number genrator between 1 and 10
number = random.randint(1, 10)
guesses = 0

while True:
   guess = input("Guess a number between 1 and 10: ")
   guess = int(guess)
   guesses += 1
    
#Checking user guess
   if guess == number:
        print("You guessed correctly!")
        break
   elif guess < number:
        print("You guessed low")
   else:
        print("You guessed high")