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

def cls():
    # Clears the console
    os.system('cls' if os.name == 'nt' else 'clear')

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
while start_game:
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
        print(
            "Welcome to Wordel. A wordle clone. This game has three different modes.")
        print(
            'The game is simple. Input a five letter word.')
        print(
            'If the letters in your guess are both in the word and in the same position')
        print(
            'It will return ' + colored(0, 255, 0, "green"))
        print(
            'If the letters in your guess are in the word but not in the same position')
        print(
            'It will return ' + colored(255, 255, 0, "Yellow"))
        print(
            'If the letter is not in the word at all. It will return ' +
            colored(255, 0, 0, 'Red'))
        print("That's it, simple right?")
        print('There are three modes you can choose!')
        print('Normal, where you only guess one word!')
        print('Hard, where you have to guess two words!')
        print('Finally, Super Hard, where you have to guess four words!')
    # sets the diffculty for the player
    challenge = input(
        "Press 1 for easy mode, 2 for hard mode and 3 for super hard mode: \n")
    # sets the max attempts for a player
    max_attempts = num_of_attempts(challenge)
    count = max_attempts + 1
    play_game = True
    while play_game:
        # sets prettytable to default
        table.clear()
        if max_attempts == 0:
            # what happens when you lose the game
            Lose = pyfiglet.figlet_format("You Lose!", justify="center")
            print(Lose)
            restart_game()
        else:
            remain = count - max_attempts
            # cheatsheet
            # print(answer1, answer2, answer3, answer4)
            # input for guess
            word = input('Guess a five letter Word: ').lower()
            if len(word) != WORD_LENGTH:
                # if the input does not work for the game
                print('You guess must have five letters')
                complete_guess = False
            else:
                # starts the logic for the game.
                complete_guess = True
                cls()
            # starts the game
            while complete_guess:
                if challenge == '2':
                    # if the game is in hard mode
                    if guess_1 == 1:
                        # if the word has been guessed it will fill the rest of the array.
                        attempts1.append(" ".join(["_"] * WORD_LENGTH))
                    else:
                        attempts1.append(guess_match(answer1, word))
                    if word == answer1:
                        # removes word from the options
                        guess_1 = 1
                    if guess_2 == 1:
                        attempts2.append(" ".join(["_"] * WORD_LENGTH))
                    else:
                        # joins the word into the array
                        attempts2.append(guess_match(answer2, word))
                    if word == answer2:
                        guess_2 = 1
                    if (guess_1 + guess_2) == 2:
                        # the player has won the game
                        win_message(remain)
                        guess_1 = 0
                        guess_2 = 0
                        max_attempts = 0
                        restart_game()
                    else:
                        # creates the table for prettytable
                        table.add_column("Hard", attempts1)
                        table.add_column('Mode', attempts2)
                        print(table)
                    complete_guess = False
                elif challenge == '3':
                    # if the game is in super hard mode
                    if guess_1 == 1:
                        attempts1.append(" ".join(["_"] * WORD_LENGTH))
                    else:
                        attempts1.append(guess_match(answer1, word))
                    if word == answer1:
                        guess_1 = 1
                    if guess_2 == 1:
                        attempts2.append(" ".join(["_"] * WORD_LENGTH))
                    else:
                        attempts2.append(guess_match(answer2, word))
                    if word == answer2:
                        guess_2 = 1
                    if guess_3 == 1:
                        attempts3.append(" ".join(["_"] * WORD_LENGTH))
                    else:
                        attempts3.append(guess_match(answer3, word))
                    if word == answer3:
                        guess_3 = 1
                    if guess_4 == 1:
                        attempts4.append(" ".join(["_"] * WORD_LENGTH))
                    else:
                        attempts4.append(guess_match(answer4, word))
                    if word == answer4:
                        guess_4 = 1

                    if (guess_1 + guess_2 + guess_3 + guess_4) == 4:
                        # The player has won the game
                        win_message(remain)
                        guess_1 = 0
                        guess_2 = 0
                        guess_3 = 0
                        guess_4 = 0
                        max_attempts = 0
                        restart_game()
                    else:
                        # creates the table for prettytable
                        table.add_column("Wordle", attempts1)
                        table.add_column('Super', attempts2)
                        table.add_column("Hard", attempts3)
                        table.add_column('Mode', attempts4)
                        print(table)
                    complete_guess = False
                else:
                    # if the game is in normal mode.
                    attempts1.append(guess_match(answer1, word))
                    table.add_column("Wordle", attempts1)
                    # prints the table from prettytable
                    print(table)
                    if word == answer1:
                        # the player has won
                        win_message(remain)
                        max_attempts = 0
                        restart_game()
                    complete_guess = False
                max_attempts -= 1
                cls()
