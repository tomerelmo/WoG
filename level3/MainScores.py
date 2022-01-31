import sys
import os
sys.path.insert(0, f"{os.getcwd()}/utils/")
from flask import Flask
from  gamesUtils import BAD_RETURN_CODE, SCORES_FILE_NAME , return_score
app = Flask(__name__)


@app.route('/')
def score_server():
    SCORE = return_score()
    if BAD_RETURN_CODE != SCORE:
        return f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{SCORE}</div></h1>
        </body>
        </html>
        """

    return f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <body>
            <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
            </body>
            </html>
            """

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

