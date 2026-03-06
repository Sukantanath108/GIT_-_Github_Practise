# list some questions
# store them in a dictionary
# choose random question everytime
# assign points for each correct answer
# track scores of user
# show them their score

import random

#dictionary have keys and values. Dict --> keys : values
questions = {
    "What is the package for visualization in machine learning": "Matplotlib",
    "what is the size of a byte?": 8,
    "1 GB equal to what ?" : "1024 MB",
    "Who is the father of biology?": "aristotle",
    "Whats 2 + 2?": 4,
    "What does the random module do?" : "generate random numbers"
}

def trivia_game():
    print("This is the trivia game!\n")
    ques_list = list(questions.keys())
    # print(ques_list)
    ques_values = list(questions.values())
    # print(ques_values)
    total_ques = len(ques_list)
    score = 0
    # chooses k unique random elements from a population sequence
    selected_ques = random.sample(ques_list, total_ques)


    for index,ques in enumerate(selected_ques):
        print(f"question no {index+1} is: {selected_ques[index]}")
        user_answer = input("Enter your answer: ").lower().strip() # removes extra space from users input. they type "  8", it will show 8
        if str(user_answer).lower().strip() == str(questions[ques]).lower().strip():
            print("You guessed correctly!")
            score +=1
        else:
            print(f"Sorry, incorrect. Correct answer is {questions[ques]}. Try next questions!")
    print(f"You scored {score} out of {total_ques}.")
    print("Game over")
trivia_game()

