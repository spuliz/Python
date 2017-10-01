# Write a Python program that will simulate “Guess the number” game.
# The computer thinks of a secret number between 1 and 100 (you can randomly generate
# that number). You are asked to enter your guess and the computer will print if the secret
# number is larger or smaller than the number you guessed. The game stops when you guess
# the number, or when you enter 0 to exit.

import random

secret_number = random.randint(1, 100)

while True:
#Extend your program to only allow 10 attempts. If the user doesn’t guess after 10 attempts the game ends.
    for i in range(10):
        number = int(input("Plese enter your guess or zero to exit "))
        if number == 0:
            print("Game Stopped")
            break
        elif number == secret_number:
            print("You guessed it right!")
            break
        elif number < secret_number:
            print("Too small")
        else:
            print("Too large")
    print("Game Stopped")
    break

