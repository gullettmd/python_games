"""This is a based off of the game Bagels by Al Sweigart al@inventwithpython.com. 
For this game you guess a 4 digit number then you are given clues that tell you if you got it right."""

import random

NUM_DIGITS = 4
MAX_GUESSES = 20


def main():
    print("Welcome to Yes, No and Maybe!")
    print("\nThis is a deducive logic game where you try to guess my number.")
    print("\nI have thought of a 4-digit number, each digit is different. Make a guess by typing a 4-digit number and I'll give you clues for which digits in my number you guessed right.")
    print('''\nHere are your clues. If I say:
       Yes - One digit is right and in the right spot.
       No - None of the digits are right.
       Maybe - One of the digits you guessed is right but in the wrong spot.''')

    print("\nFor example, let's say my number was 2481 and you guessed  8436, I would give the clues: Maybe Yes.".format(NUM_DIGITS))

    while True:  # Game loop
        # Store the secret number:
        secretNum = getSecretNum()
        print("\nI with think of a number.....")
        print("\nHmmmmmmm..... Let me see...")
        print("\nI thought up a number! This should be good!")
        print("\nYou have {} chances to guess my number.".format(MAX_GUESSES))
