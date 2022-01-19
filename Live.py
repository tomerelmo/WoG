import GuessGame
import MemoryGame
import CurrencyRouletteGame
from time import sleep
game_difficulty = 0
choose_game = 0


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


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

        if choose_game.isnumeric():
            choose_game = int(choose_game)
            if choose_game == 1:
                print("\n[+]You choose : Memory Game")
                if MemoryGame.play(game_difficulty):
                    print("\n[+]You Won The Memory Game!!")
                    sleep(2)
                    continue
                else:
                    print("\n[-]You Lost Memory Game you peace of shit! you'r worthless!")
                    sleep(2)
                    continue

            elif choose_game == 2:
                print("\n[+]You choose : Guess Game")
                if GuessGame.play(game_difficulty):
                    print("\n[+]You Won The Guess Game!!")
                    sleep(2)
                    continue
                else:
                    print("\n[-]You Lost Guess Game you peace of shit! you'r worthless!")
                    sleep(2)
                    continue
            elif choose_game == 3:
                print("\n[+]You choose : Currency Roulette")
                if CurrencyRouletteGame.play(game_difficulty):
                    print("\n[+]You Won The Currency Roulette!!")
                    sleep(2)
                    continue
                else:
                    print("\n[-]You Lost Currency Roulette game you peace of shit! you'r worthless!")
                    sleep(2)
                    continue
            else:
                print("\n[-]Error :Unsupported game, Pick number between 1-3 ,running main menu again-- >")
                continue
        else:
            print("\n[-]Error : Unsupported choose, Pick number between 1-3, Please start over. ")
            continue






