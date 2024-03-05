# Code begins line 57

"""
In a file called mario.py in a folder called sentimental-mario-more, write a program that recreates a 
half-pyramid using hashes (#) for blocks, exactly as you did in Problem Set 1. Your program this time 
should be written in Python!

Specification
    To make things more interesting, first prompt the user with get_int for the half-pyramid's height, 
    a positive integer between 1 and 8, inclusive. (The height of the half-pyramids pictured above happens 
    to be 4, the width of each half-pyramid 4, with a gap of size 2 separating them).
    If the user fails to provide a positive integer no greater than 8, you should re-prompt for the same again.
    Then, generate (with the help of print and one or more loops) the desired half-pyramids.
    Take care to align the bottom-left corner of your pyramid with the left-hand edge of your terminal window, 
    and ensure that there are two spaces between the two pyramids, and that there are no additional spaces after 
    the last set of hashes on each row.

How to Test
> Run your program as python mario.py and wait for a prompt for input. Type in -1 and press enter. 
  Your program should reject this input as invalid, as by re-prompting the user to type in another number.
> Run your program as python mario.py and wait for a prompt for input. Type in 0 and press enter. 
  Your program should reject this input as invalid, as by re-prompting the user to type in another number.
> Run your program as python mario.py and wait for a prompt for input. Type in 1 and press enter. 
  Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, 
  and that there are no extra spaces at the end of each line.

  #  #

> Run your program as python mario.py and wait for a prompt for input. Type in 2 and press enter. Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.
     #  #
    ##  ##
> Run your program as python mario.py and wait for a prompt for input. Type in 8 and press enter. Your program should generate the below output. Be sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.

       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########

> Run your program as python mario.py and wait for a prompt for input. Type in 9 and press enter. 
  Your program should reject this input as invalid, as by re-prompting the user to type in another number. 
  Then, type in 2 and press enter. Your program should generate the below output. Be sure that the pyramid 
  is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.

 #  #
##  ##

> Run your program as python mario.py and wait for a prompt for input. Type in foo and press enter. 
  Your program should reject this input as invalid, as by re-prompting the user to type in another number.
> Run your program as python mario.py and wait for a prompt for input. Do not type anything, and press enter. 
  Your program should reject this input as invalid, as by re-prompting the user to type in another number.
"""

def main():
    # While loop to ask for correct input repeatedly until given
    while True:
        # Try block to handle exceptions
        try:
          height = int(input("Height: "))
          # Checks that value is between expected parameters, breaks if met to continue program 
          if height > 0 and height <= 8:
              break
        # Exception to handle non-integer inputs such as strings
        except:
            print("Error: Please input an integer of 1-8")
            pass

    # hash must always be set to 1 to begin the loop no matter the size
    hashes = 1
    # space is set as height - hash so that the correct amount of spaces can be displayed. 
    # If height is 1 then spaces is zero and will not be output, if height is 8, then spaces is 7.
    spaces = height - hashes

    for i in range(height):
        # Spaces are set first, new line is ignored. Spaces multiplies a " " to give correct amount, if 0 nothing is produced
        print(spaces * " ", end="")
        # Hashes is then displayed, with a tab to seperate the next set of hashes
        print(hashes * "#", end="  ")
        # Final hashes set for the right step
        print(hashes * "#")
        # Iterates over hash and space variables, adding additional hashes and reducing spaces for next line
        hashes += 1
        spaces -= 1
        
main()
