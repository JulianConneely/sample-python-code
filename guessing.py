# Julian Conneely, 2018-02-14
# Guessing Game

from random import randint

target = randint(1, 100)
guess = 101

print("Guess a number between 1 and 100.")
while guess != target:
    guess = int(input("Please enter your guess: "))
    if guess == target:
        print("Well done! You guessed correctly.")
    elif guess < target:
            print("Too low!")
    else:
            print("Too high")
