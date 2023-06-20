def quiz(question, correct_answers, score):
    user_answer = input(question + " ")
    if user_answer.lower() in correct_answers:
        print("Correct!")
        return score
    else:
        print("Incorrect! The correct answer(s) is/are:", ", ".join(correct_answers))
        return 0

score = 0

print("Welcome to the Quiz!")
level_choice = int(input("Choose a level: 1 or 2: "))

# Level 1 Questions
if level_choice == 1:
    print("Level 1 - Good luck!")
    
    question1 = "What do we call a mother lion?"
    correct_answers1 = ["lioness"]
    score += quiz(question1, correct_answers1, 1)

    question2 = "What is the capital of France?"
    correct_answers2 = ["paris"]
    score += quiz(question2, correct_answers2, 1)

    question3 = "What is the largest planet in our solar system?"
    correct_answers3 = ["jupiter"]
    score += quiz(question3, correct_answers3, 1)

    question4 = "What is the chemical symbol for gold?"
    correct_answers4 = ["au"]
    score += quiz(question4, correct_answers4, 1)

    question5 = "What is the tallest mountain in the world?"
    correct_answers5 = ["mount everest", "everest"]
    score += quiz(question5, correct_answers5, 1)

    question6 = "Who painted the Mona Lisa?"
    correct_answers6 = ["leonardo da vinci"]
    score += quiz(question6, correct_answers6, 1)

    question7 = "What is the largest ocean on Earth?"
    correct_answers7 = ["pacific ocean", "pacific"]
    score += quiz(question7, correct_answers7, 1)

    question8 = "What is the symbol for the element oxygen?"
    correct_answers8 = ["o"]
    score += quiz(question8, correct_answers8, 1)

    question9 = "What is the capital of Japan?"
    correct_answers9 = ["tokyo"]
    score += quiz(question9, correct_answers9, 1)

    question10 = "Who wrote the play 'Romeo and Juliet'?"
    correct_answers10 = ["william shakespeare", "shakespeare"]
    score += quiz(question10, correct_answers10, 1)

    print("Congratulations! You have completed Level 1.")
    level_choice = int(input("Proceed to Level 2? Enter 2 to continue: "))

# Level 2 Questions
if level_choice == 2:
    print("Level 2 - Good luck!")

    question11 = "What is the largest continent?"
    correct_answers11 = ["asia"]
    score += quiz(question11, correct_answers11, 2)

    question12 = "Which planet is known as the 'Red Planet'?"
    correct_answers12 = ["mars"]
    score += quiz(question12, correct_answers12, 2)

    question13 = "What is the capital of Australia?"
    correct_answers13 = ["canberra"]
    score += quiz(question13, correct_answers13, 2)

    question14 = "Who is the author of the Harry Potter book series?"
    correct_answers14 = ["j.k. rowling", "rowling"]
    score += quiz(question14, correct_answers14, 2)

    question15 = "Which country is known as the 'Land of the Rising Sun'?"
    correct_answers15 = ["japan"]
    score += quiz(question15, correct_answers15, 2)

    question16 = "What is the chemical symbol for silver?"
    correct_answers16 = ["ag"]
    score += quiz(question16, correct_answers16, 2)

    question17 = "Who is the Greek god of thunder?"
    correct_answers17 = ["zeus"]
    score += quiz(question17, correct_answers17, 2)

    question18 = "What is the largest desert in the world?"
    correct_answers18 = ["sahara"]
    score += quiz(question18, correct_answers18, 2)

    question19 = "Who is the current President of the United States?"
    correct_answers19 = ["joe biden", "biden"]
    score += quiz(question19, correct_answers19, 2)

    question20 = "Which famous scientist developed the theory of general relativity?"
    correct_answers20 = ["albert einstein", "einstein"]
    score += quiz(question20, correct_answers20, 2)

    print("Congratulations! You have completed Level 2.")

print("Your final score is:", score)
def quiz(question, correct_answers, score):
    user_answer = input(question + " ")
    if user_answer.lower() in correct_answers:
        print("Correct!")
        return score
    else:
        print("Incorrect! The correct answer(s) is/are:", ", ".join(correct_answers))
        return 0

score = 0

# Level 1 Questions
question1 = "What do we call a mother lion?"
correct_answers1 = ["lioness"]
score += quiz(question1, correct_answers1, 1)

question2 = "What is the capital of France?"
correct_answers2 = ["paris"]
score += quiz(question2, correct_answers2, 1)

question3 = "What is the largest planet in our solar system?"
correct_answers3 = ["jupiter"]
score += quiz(question3, correct_answers3, 1)

question4 = "What is the chemical symbol for gold?"
correct_answers4 = ["au"]
score += quiz(question4, correct_answers4, 1)

question5 = "What is the tallest mountain in the world?"
correct_answers5 = ["mount everest", "everest"]
score += quiz(question5, correct_answers5, 1)

question6 = "Who painted the Mona Lisa?"
correct_answers6 = ["leonardo da vinci"]
score += quiz(question6, correct_answers6, 1)

question7 = "What is the largest ocean on Earth?"
correct_answers7 = ["pacific ocean", "pacific"]
score += quiz(question7, correct_answers7, 1)

question8 = "What is the symbol for the element oxygen?"
correct_answers8 = ["o"]
score += quiz(question8, correct_answers8, 1)

question9 = "What is the capital of Japan?"
correct_answers9 = ["tokyo"]
score += quiz(question9, correct_answers9, 1)

question10 = "Who wrote the play 'Romeo and Juliet'?"
correct_answers10 = ["william shakespeare", "shakespeare"]
score += quiz(question10, correct_answers10, 1)

# Level 2 Questions
question11 = "What is the largest continent?"
correct_answers11 = ["asia"]
score += quiz(question11, correct_answers11, 2)

question12 = "Which planet is known as the 'Red Planet'?"
correct_answers12 = ["mars"]
score += quiz(question12, correct_answers12, 2)

question13 = "What is the capital of Australia?"
correct_answers13 = ["canberra"]
score += quiz(question13, correct_answers13, 2)

question14 = "Who is the author of the Harry Potter book series?"
correct_answers14 = ["j.k. rowling", "rowling"]
score += quiz(question14, correct_answers14, 2)

question15 = "Which country is known as the 'Land of the Rising Sun'?"
correct_answers15 = ["japan"]
score += quiz(question15, correct_answers15, 2)

question16 = "What is the chemical symbol for silver?"
correct_answers16 = ["ag"]
score += quiz(question16, correct_answers16, 2)

question17 = "Who is the Greek god of thunder?"
correct_answers17 = ["zeus"]
score += quiz(question17, correct_answers17, 2)

question18 = "What is the largest desert in the world?"
correct_answers18 = ["sahara"]
score += quiz(question18, correct_answers18, 2)

question19 = "Who is the current President of the United States?"
correct_answers19 = ["joe biden", "biden"]
score += quiz(question19, correct_answers19, 2)

question20 = "Which famous scientist developed the theory of general relativity?"
correct_answers20 = ["albert einstein", "einstein"]
score += quiz(question20, correct_answers20, 2)

print("Your final score is:", score)
