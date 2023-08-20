import random
import time
import os
from monster import monster
from monster import bigger_monster
from monster import biggest_monster

#Intro
name = input("Hello Adventurer, what is your name? ")

#Create starting character teplate
character = {
    "charname": name,
    "lvl": 1,
    "xp": 0,
    "hp": 20,
    "dmg": 2,
}

#Explain the game
os.system('cls')
time.sleep(2)
print("Welcome " + character["charname"] + " to The Tower.")
time.sleep(2)
print("Once you have vanquished the foes on this level, you will proceed to the one above.")
time.sleep(2)
print("Fight your way to the top to be crowned Champion.\nGood luck!")
time.sleep(5)
os.system('cls')
time.sleep(2)

#Start lvl 1
print("TOWER LEVEL 1")
time.sleep(2)

#encounter function to pick enemies based on char level
def encounter():
    if character["lvl"] < 3:
        enemy = monster()
    elif character["lvl"] < 5:
        enemy = bigger_monster()
    elif character["lvl"] < 7:
        enemy = biggest_monster()

    print("A " + enemy.this_monster["type"] + " appears!")

encounter()
    