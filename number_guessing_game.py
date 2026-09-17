import random

secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! 🎉")
        print("You got it in", attempts, "attempts!")
