"""This is a Bitmap Message inspired by Al Sweigart al@inventwithpython.com
The code will show a message based on the bitmap image created."""

import sys
import time

# The original bitmap can be copy/pasted from:
# https://inventwithpython.com/bitmapworld.txt
# The original image was a map of Earth.)
bitmap = """
.....................................................


                    ************
               ******          ******
           *****                    *****
        ****                            ****
      **                                    **
     **                                      **
    **         ***               ***         **
   **          ***               ***          **
   **                                         **
   **                   ***                   **
   **                   ***                   **
   **                                         **
    **      **                      **       **
     **      ***                  ***       **
      **       ***              ***        **
       ****       **************       ****
          ***                         ***
            *****                 *****
                 *****************
                 
     
....................................................."""

print('Smile!')
time.sleep(1)
print('What message would you like to show on the bitmap?')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    time.sleep(.25)
    print()  # Print a newline.
