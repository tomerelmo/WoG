import sys
import os
sys.path.insert(0, f"{os.getcwd()}/games")
sys.path.insert(0, f"{os.getcwd()}/utils")
import GuessGame
import MemoryGame
import CurrencyRouletteGame
from score import add_score
from time import sleep
from gamesUtils import screen_cleaner
game_difficulty = 0
choose_game = 0


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def game_win(gameName, game_difficulty):
    print(f"\n[+]You Won The {gameName}!!")
    add_score(game_difficulty)
    sleep(2)
    screen_cleaner()


def load_game():
    global game_difficulty , choose_game
    main_menu_running = True
    while main_menu_running :
        print("""\nPlease choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")
        choose_game = input("\nEnter The number of the game your want -->  ")
        game_difficulty = input("Enter The number of the game difficulty want \nPick number from 1-5 --> ")
        if game_difficulty.isnumeric():
            if 0 < int(game_difficulty) < 6:
                print(f"\n[+]Your Game difficulty will be : {game_difficulty} .")
                game_difficulty = int(game_difficulty)
            else:
                print("\n[-]Error :Unsupported difficulty, Pick number between 1-5 ,running main menu again-- >")
                break
        games_dict = {
            1: "Memory Game",
            2: "Guess Game",
            3: "Currency Roulette"
        }
        if choose_game.isnumeric():
            choose_game = int(choose_game)

            print(f"\n[+]You choose : {games_dict[choose_game]}")
            if choose_game == 1:
                if MemoryGame.play(game_difficulty):
                    game_win(games_dict[choose_game], game_difficulty)
                    continue
            if choose_game == 2:
                if GuessGame.play(game_difficulty):
                    game_win(games_dict[choose_game], game_difficulty)
                    continue
            if choose_game == 3:
                if CurrencyRouletteGame.play(game_difficulty):
                    game_win(games_dict[choose_game], game_difficulty)
                    continue
            else:
                print("\n[-]You Lost Memory Game you peace of shit! you'r worthless!")
                sleep(2)
                screen_cleaner()
                continue
        else:
            print("\n[-]Error :Unsupported game, Pick number between 1-3 ,running main menu again-- >")
            continue
    else:
        print("\n[-]Error : Unsupported choose, Pick number between 1-3, Please start over. ")







