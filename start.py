import random
from monster import monster

name = input("Hello Adventurer, what is your name? ")

character = {
    "charname": name,
    "lvl": 1,
    "xp": 0,
    "hp": 20,
    "dmg": 2,
}

print(character)

#def encounter():