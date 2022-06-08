# import the word list
from word_list import word_list
# import random module
import random
# import prettytable
from prettytable import PrettyTable
# import os module
import os
# import pyfiglet
import pyfiglet

# Word length variable
WORD_LENGTH = 5
# initialise all the arrays
attempts1 = []
attempts2 = []
attempts3 = []
attempts4 = []
# create the variables for the guesses
guess_1 = 0
guess_2 = 0
guess_3 = 0
guess_4 = 0
complete_guess = True
# create the table from prettytable
table = PrettyTable()


# functions
# Allows the letters to be colored in the terminal.
def colored(r, g, b, text):
  return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# returns the result of comparing the guess with the set answer
def guess_match(theanswer, theguess):
  count = 0
  clue = ''
  for letter in theguess:
    if letter == theanswer[count]:
      clue += colored(0, 255, 0, letter.upper())
    elif letter in theanswer:
      clue += colored(255, 255, 0, letter )
    else:
      clue += colored(255, 0, 0, letter)
    count += 1
  return clue

# takes which mode the player chose and returns the number of turns
def num_of_attempts(challenge):
  if challenge == '1':
    return 6
  elif challenge == '2':
    return 7
  elif challenge == '3':
    return 8
  else:
    return 6

# restarts the game and initialises everything back to 0
def restart_game():
  restart = input('Would you like to play again. Y or N')
  global start_game, play_game, attempts1, attempts2, attempts3, attempts4
  if restart.lower() == 'n':
    start_game = False
    play_game = False
  else:
    play_game = False
    attempts1.clear()
    attempts2.clear()
    attempts3.clear()
    attempts4.clear()