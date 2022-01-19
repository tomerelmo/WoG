# This game will use t he free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
# Properties
# 1. Difficulty
# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import requests
import random
from currency_converter import CurrencyConverter


def get_money_interval(difficultly):
    convert  = CurrencyConverter()
    random_usd = random.randint(1, 100)
    generated_random_usd = convert.convert(random_usd, 'USD', 'ILS')
    print(generated_random_usd)
    if str(generated_random_usd).split(".")[0].isnumeric():
        print(f"[+]Usd amount IS : {random_usd}")
        num1 = generated_random_usd - (5 - difficultly)
        num2 = generated_random_usd + (5 - difficultly)
        return [num1 , num2]
    else:
        print("[-]Error : Bad API answer please start over, check internet connection and credentials. ")
        pass


def get_guess_from_user(nums_lst):
    user_input = input("[+]Guess The ILS amount of USD presented above :")
    if user_input.isnumeric():
        user_input = float(user_input)
        if nums_lst[0] <= user_input <= nums_lst[1]:
            return True
        else:
            return False
    else:
        print("[-]Error : User input is wrong, Please start over. ")
        pass


def play(difficultly):
    if get_guess_from_user(get_money_interval(difficultly)):
        return True
    else:
        return False


#test!
# print(type(get_money_interval(difiiculty)))
# print(play(difiiculty))