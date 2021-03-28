# Arithmetic Computational Game - Zoo-o-mathematics!
import random 
# --- function definitions ---
# diff 1: 1, 2, 3, 4 (beginner)
# diff 2: 5, 6, 7, 8 (intermediate)
# diff 3: 9, 10, 11, 12 (advanced)

# --- addition ---
def random_addition(d, loop):
    if d == 1:
        result = random_add1(loop)
    elif d == 2:
        result = random_add2(loop)
    else:
        result = random_add3(loop)
    return result

def random_add1(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(1, 4)
        num2 = random.randint(1, 4)
        sol = num1 + num2
        print("What is {} + {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

def random_add2(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(5, 8)
        num2 = random.randint(5, 8)
        sol = num1 + num2
        print("What is {} + {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop

def random_add3(loop):
    num_correct = 0
    for i in range(loop):    
        num1 = random.randint(9, 12)
        num2 = random.randint(9, 12)
        sol = num1 + num2
        print("What is {} + {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 
# -- subtraction ---
def random_subtraction(d,loop):
    if d == 1:
        result = random_sub1(loop)
    elif d == 2:
        result = random_sub2(loop)
    else:
        result = random_sub3(loop)
    return result

def random_sub1(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(1, 4)
        num2 = random.randint(1, 4)
        while (num2 > num1):         
            num2 = random.randint(1, 4)
        sol = num1 - num2
        print("What is {} - {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

def random_sub2(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(5, 8)
        num2 = random.randint(5, 8)
        while (num2 > num1):         
            num2 = random.randint(5, 8)
        sol = num1 - num2
        print("What is {} - {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

def random_sub3(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(9, 12)
        num2 = random.randint(9, 12)
        while (num2 > num1):         
            num2 = random.randint(9, 12)
        sol = num1 - num2
        print("What is {} - {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 
    
# --- multiplication ---
def random_multiplication(d, loop):
    if d == 1:
        result = random_mul1(loop)
    elif d == 2:
        result = random_mul2(loop)
    else:
        result = random_mul3(loop)
    return result

def random_mul1(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(1, 4)
        num2 = random.randint(1, 4)
        sol = num1 * num2
        print("What is {} * {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

def random_mul2(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(5, 8)
        num2 = random.randint(5, 8)
        sol = num1 * num2
        print("What is {} * {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

def random_mul3(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(9, 12)
        num2 = random.randint(9, 12)
        sol = num1 * num2
        print("What is {} * {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

# --- division ---   
def random_division(d,loop):
    if d == 1:
        result = random_div1(loop)
    elif d == 2:
        result = random_div2(loop)
    else:
        result = random_div3(loop)
    return result
        
def random_div1(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(1, 4)
        num2 = random.randint(1, 4)
        while 0 != (num1 % num2):
            num2 = random.randint(1, 4)
        sol = num1 / num2
        print("What is {} / {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 

def random_div2(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(5, 8)
        num2 = random.randint(5, 8)
        while 0 != (num1 % num2):
            num2 = random.randint(5, 8)
        sol = num1 / num2
        print("What is {} / {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 
    
def random_div3(loop):
    num_correct = 0
    for i in range(loop):
        num1 = random.randint(9, 12)
        num2 = random.randint(9, 12)
        while 0 != (num1 % num2):
            num2 = random.randint(9, 12)
        sol = num1 / num2
        print("What is {} / {} ?".format(num1, num2))
        if (sol == int(input("Enter your answer: "))):
            print("Correct!")
            num_correct += 1
        else:
            print("Incorrect. The correct answer is: {}".format(sol))
    return num_correct / loop 
    
def random_mix(d, loop):
    result = 0
    for i in range(loop):
        choice = random.randint(0, 3)
        if choice == 0:
            result += random_addition(d, 1)
        elif choice == 1:
            result += random_subtraction(d, 1)
        elif choice == 2:
            result += random_multiplication(d, 1)
        else:
            result += random_division(d, 1)
    return result / loop