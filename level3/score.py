import os
from gamesUtils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, "r")
        score = file.read()
        file.close()
        if score.isnumeric():
            new_score = POINTS_OF_WINNING + int(score)
            file = open(SCORES_FILE_NAME, "w")
            file.truncate(0)
            file.close()
            file = open(SCORES_FILE_NAME, "w")
            file.write(str(new_score))
            file.close()
        else:
            new_score = POINTS_OF_WINNING
            file = open(SCORES_FILE_NAME, "w")
            file.write(str(new_score))
            file.close()





#test
#print(add_score(3))
