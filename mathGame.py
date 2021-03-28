# Arithmetic Computational Game - Zoo-o-mathematics!

from arithmeticFunc import *
from menu import *

# ----------------- INTRO --------------------
print("What is your name?")
yourName = input("Enter your name: \n")
print("\nWelcome to " + yourName + "'s Zoo!")
# --------------------------------------------
print("You've been given the keys to a new zoo!")
print("We need your help in welcoming new friends to our zoo!")
print("In order to gain attraction to our zoo, we will need to solve some math equations together to acquire more friends!")
print("Are you ready?")
# ------------------ DIFF ---------------------
difficulty = 0

diff = True
choose_diff()
while diff:
    answer = int(input("What is your skill level fellow Zoo Keeper?\n"))
    if answer < 1  or answer > 3:
        print("Enter a valid level.")
    else:
        difficulty = answer
        diff = False

# ------------------ MENU --------------------
intro = True

while intro:
    show_intro()
    answer = input("What arithmetic operation would you like to work on?\n")

    if answer == "1":
        print("The following questions will generate addition problems.")
        print("Good luck!")
        for i in range(3):
            random_addition()
    elif answer == "2":
        print("The following questions will generate subtraction problems.")
        print("Good luck!")
        for i in range(3):
            random_subtraction()
    elif answer == "3":
        print("The following questions will generate multiplication problems.")
        print("Good luck!")
        for i in range(3):
            random_multiplication()
    elif answer == "4":
        print("The following questions will generate division problems.")
        print("Good luck!")
        for i in range(3):
            random_division()
    elif answer == "5":
        print("The following questions will generate all arithmetic operational problems:" 
                ,"addition, subtraction, multiplication, division.")
        print("Good luck!")
        for i in range(3):
            random_mix()
    elif answer == "0":
        print("We will now end the game. Thank you for playing!")
        print("Join us again in creating your own wonderful zoo!")
        var = False
    else:
        print("Please input a valid number.")

# --------------------------------------------


    