# Python quiz game
# we re using tuples bcs its immutable. if theres a possibility to use tuples, use them

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmos: ",
             "How many bones are in the human body: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A.116", "B. 117", "C.118", "D. 119"),
           ("A. Whale", "B.Crocs", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A.206", "B. 207", "C. 208", "D.209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
# this will store the correct answer for the corresponding questions
answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print(question)
    print("-" * 50)

    for option in options[question_num]:
        print(option)


    guess = input("A,B,C,D?").upper()

    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("You are corrct")
    else:
        print(f"Wrong, the right answer is  {answers[question_num]}")


    question_num += 1

print(guesses)

print("RESULTS")
print("-"* 50)

print("Answers:", end = " ")
for answer in answers:
    print(answer, end=" ")

print()

print("Your guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")

print()

print("-"* 50)

score = int(score/ len(questions) * 100)
print(f"Your score {score}%")






# for question in questions:
#     print("-"*50)
#     print(question)
#
#     # print all options in options
#     for option in options[question_num]:
#         print(option)
#         # print(question_num)
#     guess = input("Enter (A, B, C,D)").upper()
#
#     guesses.append(guess)
#
#     if guess == answers[question_num]:
#         print("Youre correct")
#     else:
#         print("Incorrect")
#         print(f"Answer is {answers[question_num]}is the correct answer")
#     question_num += 1




