# GuessGame.py
# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the
# Properties
# 1. Difficulty
# 2. Secret number
# Methods
# 1. generate_number - Will generate number between 1 to difficulty and save it to
# secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
# return the number.
# 3. compare_results - Will compare the the secret generated number to the one prompted
# by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import random
import Live

# game = Live.load_game()
# choose_game = Live.choose_game
# difficulty = Live.game_difficulty
from time import sleep


def generate_number(difficulty):
    if difficulty >= 1:
        secret_number = random.randint(1, difficulty)
        return secret_number
    else:
        print("[-]Error - Difficulty has been initialized to 1 because your entered wrong input")
        secret_number = 1
        return secret_number


def get_guess_from_user(difficulty):
    guessed_number = int(input(f"[+]Enter number from 1 to {difficulty} --- >"))
    if guessed_number <= difficulty:
        return guessed_number
    else:
        print("[-]Error - Wrong input")


def compare_results(difficulty):
    return generate_number(difficulty) == get_guess_from_user(difficulty)


def play(difficulty):
    if str(difficulty).isnumeric():
        generate_number(difficulty)
        return compare_results(difficulty)
    else:
        print("[-]Wrong number or invalid input Please start over!")
        sleep(2)

#TEST!

# print(difficulty)
# print(secret_number)
# print(get_guess_from_user(difficulty))
# print(play())