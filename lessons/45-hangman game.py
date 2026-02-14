# Hangman in Python
import random

# dictionary of {key:tuple}
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\ ")}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
        print()


def display_hint(past, answer):

    hint = ""
    correct = 0
    
    for s in answer:
        is_checked = False
        for c in past:
            if (s == c):
                hint +=  s + " " # string such as XXpXe
                correct += 1
                is_checked = True
        
        if not is_checked:
            hint += "_ "
        
         
    print(hint)
    print("*************************")

    return correct




def display_answer(ans):
    print()
    print(f"answer is: {ans}")
    print("Congratulation!")


def main():
    words = ("apple", "orange", "banana", "coconuts", "pineapple")
    word = random.choice(words)

    print("**********************************")
    print("* Welcome to Python Hangman Game *")
    print("**********************************")
    print()

    wrong_guess = 0
    correct = 0
    past = ""

    while True:
        char = input("Guess the character: ")
        print()

        # if its alphabet and one character
        if char.isalpha() and len(char) == 1:
            char = char.lower()

            if char in past:
                print("You answered that before.")
            elif char in word:
                past += char
            else:
                wrong_guess += 1
            display_man(wrong_guess)
            correct = display_hint(past, word)
            if (wrong_guess >= 6):
                print("You lost...")
                break
        else:
            print("Invalid Input")
        
        if correct == len(word):
            display_answer(word)
            break


if __name__ == "__main__":
    main()
    



