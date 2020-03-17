
import requests
import json
import pprint
import random
import html

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"
endGame = ""
while endGame != "quit":
    rqst = requests.get(url)
    if (rqst.status_code != 200):
        endGame = input("Sorry! There was a problem retrieving the question. Press enter to try again or type 'quit' to end the game.")
    else:
        valid_ans = False
        ans_num = 1
        data = json.loads(rqst.text)
        question = data['results'][0]['question']
        ans = data['results'][0]['incorrect_answers']
        correct_ans = data['results'][0]['correct_answer']
        ans.append(correct_ans)
        random.shuffle(ans)

        print(html.unescape(question) + "\n")

        for answer in ans:
            print(str(ans_num) + ") " + html.unescape(answer))
            ans_num += 1

        while valid_ans == False:
            user_ans = input("\nYour answer: ")
            try:
                user_ans = int(user_ans)
                if user_ans > len(ans) or user_ans <= 0:
                    print("Invalid answer")
                else:
                    valid_ans = True
            except:
                print("Invalid entry. Use only numbers")
        
        user_ans = ans[int(user_ans)-1]

        if user_ans == correct_ans:
            print("\nCongratulations! You answered correctly. The correct answer is: " + html.unescape(correct_ans))
            score_correct += 1
        else:
            print("Sorry,  " + html.unescape(correct_ans) + " is the correct answer.")
            score_incorrect += 1

        print("\n#####################")
        print("Your score is: " + str(score_correct))
        print("Your incorrect_score is: " + str(score_incorrect))
        print("######################")
        endGame = input("\nPress 'enter' to play again or type 'quit' to quit the game.\n").lower()

print("Thanks for playing")
        
        
            
        
