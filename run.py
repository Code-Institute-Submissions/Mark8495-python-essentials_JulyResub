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
            clue += colored(255, 255, 0, letter)
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


# prints out a win message once the words have been guessed.
def win_message(remain):
    win = pyfiglet.figlet_format("You Win!", justify="center")
    print(win)
    print('Woo you got all the answers')
    print(f'You got it in {remain} guesses')


# Welcome Message
welcome = pyfiglet.figlet_format("Wordel", justify="center")
print(welcome)
print("Word guessing command line game".center(80) + "\n")
print("Created by Mark Byrne".center(80) + "\n")

# sets initial values for game.
start_game = True
play_game = False
while start_game == True:
    # creates the random word answers
    answer1 = random.choice(word_list)
    answer2 = random.choice(word_list)
    if answer2 == answer1:
        answer2 = random.choice(word_list)
    answer3 = random.choice(word_list)
    if answer3 == answer2:
        answer3 = random.choice(word_list)
    answer4 = random.choice(word_list)
    if answer4 == answer3:
        answer4 = random.choice(word_list)
# choose to see instructions or play.
    start = input(
        'Press 1 to learn how to play, press 2 to choose difficulty: \n')
    if start == '1':
        #   instructions on how to play
        print("Welcome to Wordel. A wordle clone. This game has three different modes.")
        print('The game is simple. Input a five letter word.')
        print('If the letters in your guess are both in the word and in the same position')
        print('It will return ' + colored(0, 255, 0, "green"))
        print('If the letters in your guess are in the word but not in the same position')
        print('It will return ' + colored(255, 255, 0, "Yellow"))
        print('If the letter is not in the word at all. It will return ' +
              colored(255, 0, 0, 'Red'))
        print("That's it, simple right?")
        print('There are three modes you can choose!')
        print('Normal, where you only guess one word!')
        print('Hard, where you have to guess two words!')
        print('Finally, Super Hard, where you have to guess four words!')
