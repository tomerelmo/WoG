import os

if "utils" in os.path.dirname("\\"):
    if os.name == 'nt':
        SCORES_FILE_NAME = "scores.txt"
    else:
        SCORES_FILE_NAME = f"{os.getcwd()}/scores.txt"
else:
    SCORES_FILE_NAME = f"{os.getcwd()}/utils/scores.txt"

BAD_RETURN_CODE = -90


def screen_cleaner():
    print ("\n"*100)


def return_score():
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME,"r+")as file:
            score = file.read()
            if score.isnumeric():
                return int(score)
    return BAD_RETURN_CODE


#screen_cleaner()