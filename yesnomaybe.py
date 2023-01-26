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

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
          guess = ''
          # loop until they make valid guess:
          while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('Guess #{}: '.format(numGuesses))
            guess = input('> ')

          clues = getClues(guess, secretNum)
          print(clues)
          numGuesses += 1

          if guess == secretNum:
            break  # break the loop when guessed correctly.
          if numGuesses > MAX_GUESSES:
            print('Sorry, you ran out of guesses.')
            print('My number is {}.'.format(secretNum))

        # Ask to play again:
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
          break  # no response or "no" means they don't want to play again. Response starting with "y" means they do.
      print("Thanks for playing! Hope to see you again!")

    
def getSecretNum():
      numbers = list('0123456789')  # list of digits 0-9.
      random.shuffle(numbers)  # Shuffle the numbers into a random order.

      # Get the first NUM_DIGITS digit in the list for the secret number:
      secretNum = ''
      for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
      return secretNum

def getClues(guess, secretNum):
  """Returns a string with the Yes, No, Maybe."""
  if guess == secretNum:
    return 'You got it!'

  clues = []

  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      # A correct digit is in the correct place.
      clues.append('Yes')
    elif guess[i] in secretNum:
      # A correct digit is in the incorrect place.
      clues.append('Maybe')
  if len(clues) == 0:
    return 'No'  # There are no correct digits at all.
  else:
    # Sort the clues into alphabetical order so their original order
    # doesn't give information away.
    clues.sort()
    
    # Make a single string from the list of string clues.
    return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
  main()
    
    
