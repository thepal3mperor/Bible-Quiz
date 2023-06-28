import random

# Bible questions and answers
bible_questions = {
    "Who built the ark?": "Noah",
    "Who was swallowed by a big fish?": "Jonah",
    "Who was the first man in the Bible?": "Adam",
    "Who killed Goliath?": "David",
    "Who was the mother of Jesus?": "Mary"
}

# Function to ask a random question
def ask_question():
    question = random.choice(list(bible_questions.keys()))
    answer = bible_questions[question]
    
    user_answer = input(question + " (Enter 'q' to quit) ")
    
    if user_answer.lower() == 'q':
        return 'q'
    elif user_answer.lower() == answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answer)

# Main program loop
while True:
    print("Welcome to St Austin's Bible Quiz!")
    print("Type 'q' to quit.")
    print()
    
    result = ask_question()
    
    if result == 'q':
        break
    
    play_again = input("Do you want to play again? (yes/no) ")
    
    if play_again.lower() == "no":
        break

print("This program was developed by namodrew7@gmail.com. Thank you for playing!")
