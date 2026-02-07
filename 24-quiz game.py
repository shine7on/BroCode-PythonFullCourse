questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. whale", "B. crocodile", "C. elephant", "D. ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. mercury", "B. venus", "C. earth", "D. mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0




for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Select A, B, C, or D: ").upper()
    while guess != "A" and guess != "B" and guess != "C" and guess != "D":
        guess = input("Select A, B, C, or D: ")
    guesses.append(guess)
    question_num += 1
    print()


for x in range(0,len(guesses)):
    if guesses[x] == answers[x]:
        score += 1

print(guesses)
print(score)


'''
for x in range(0,len(questions)):
    print(questions[x])
    print(options[x])
    guess = input("Select A, B, C, or D: ")
    while guess != "A" and guess != "B" and guess != "C" and guess != "D":
        guess = input("Select A, B, C, or D: ")
    guesses.append(guess)
    print()


for x in range(0,len(guesses)):
    if guesses[x] == answers[x]:
        score += 1

print(score)
'''