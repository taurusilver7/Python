
import requests
import json

url = "https://opentdb.com/api.php?amount=1"
endGame = ""
while endGame != "quit":
    rqst = requests.get(url)
    if (rqst.status_code != 200):
        endGame = input("Sorry! There was a problem retrieving the question. Press enter to try again or type 'quit' to end the game.")
