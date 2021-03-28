# Arithmetic Computational Game - Zoo-o-mathematics!
import random 
# -- function definitions ----------------
def random_addition():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    sol = num1 + num2
    print("What is {} + {} ?".format(num1, num2))
    if (sol == int(input("Enter your answer: "))):
        print("Correct!")
    else:
        print("Incorrect")

def random_subtraction():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    while (num2 > num1):         
        num2 = random.randint(1, 12)
    sol = num1 - num2
    print("What is {} - {} ?".format(num1, num2))
    if (sol == int(input("Enter your answer: "))):
        print("Correct!")
    else:
        print("Incorrect")

def random_multiplication():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    sol = num1 * num2
    print("What is {} * {} ?".format(num1, num2))
    if (sol == int(input("Enter your answer: "))):
        print("Correct!")
    else:
        print("Incorrect")
        
        
def random_division():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    while 0 != (num1 % num2):
        num2 = random.randint(1, 12)
    sol = num1 / num2
    print("What is {} / {} ?".format(num1, num2))
    if (sol == int(input("Enter your answer: "))):
        print("Correct!")
    else:
        print("Incorrect")

def random_mix():
    choice = random.randint(0, 3)
    if choice == 0:
        random_addition()
    elif choice == 1:
        random_subtraction()
    elif choice == 2:
        random_multiplication()
    else:
        random_divisi