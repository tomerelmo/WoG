import random
from time import sleep
import sys

# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
# difficulty = 2


def generate_sequence(difficulty):
    random_list = []
    for num in range(difficulty):
        random_list.append(random.randint(1,101))
    for i in range(1):
        sys.stdout.write('\r' + f"{random_list}")
        sleep(0.7)
        sys.stdout.write('\r')
    return random_list


def get_list_from_user(difficulty):
    list_from_usr = []
    for num in range(difficulty):
        user_input = input("[]Enter A number Between 1-101 :")
        if user_input.isnumeric() and 1 < int(user_input) < 101:
            list_from_usr.append(int(user_input))
        else:
            print("Wrong number or invalid input Please start over!")
            break
    if len(list_from_usr) == difficulty:
        return list_from_usr


def is_list_equal(difficulty):
    return generate_sequence(difficulty) == get_list_from_user(difficulty)



def play(difficulty):
    return is_list_equal(difficulty)



#test!
# print(is_list_equal(difficulty))
# print(play(difficulty))