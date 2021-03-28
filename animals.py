# Arithmetic Computational Game - Zoo-o-mathematics!
# set of arrays - animals for each corresponding level of difficulty

from arithmeticFunc import *

listOfAnimals = [
    "hare",
    "lion",
    "camel",
    "koala",
    "lemur",
    "otter",
    "panda",
    "sloth",
    "tiger",
    "zebra",
    "dragon",
    "gorilla",
    "jaguar",
    "penguin",
    "ostrich",
    "serpent",
    "orangutan",
    "lochness monster"
]

def getAnimal(num):
    if num >= 0.90:
        animal = random.choice(listOfAnimals)
        print("Congratulations! You have earned a new friend: ", animal.upper(), "!")
    else: 
        print("Oh shucks. Better look next time fellow Zookeeper!")

