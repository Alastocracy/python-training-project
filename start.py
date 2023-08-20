import random
import time
import os
from monster import monster
from monster import bigger_monster
from monster import biggest_monster

#Clear terminal at start
os.system('cls')

#Intro
name = input("Hello Adventurer, what is your name? ")

#Create starting character teplate
character = {
    "charname": name,
    "lvl": 1,
    "xp": 0,
    "hp": 30,
    "dmg": 3,
}

#Explain the game
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
print("FLOOR 1")
time.sleep(2)

#encounter function to pick enemies based on char level
def encounter():
    if character["lvl"] < 3:
        enemy = monster()
    elif character["lvl"] < 5:
        enemy = bigger_monster()
    elif character["lvl"] < 7:
        enemy = biggest_monster()
    
    print("From the darkness a foe approaches...")
    time.sleep(2)
    print("A " + enemy.this_monster["type"] + " appears!")

    while enemy.this_monster["hp"] > 0 and character["hp"] > 0:
        time.sleep(2)
        print("The " + enemy.this_monster["type"] + " " + enemy.this_monster["attack"] + " you for " + str(enemy.this_monster["dmg"]) +" damage.")
        enemy.this_monster["hp"] = enemy.this_monster["hp"] - character["dmg"]
        time.sleep(2)
        character["hp"] = character["hp"] - enemy.this_monster["dmg"]

        print(character["charname"] + " hit points remaining: " + str(character["hp"]) + ", " + enemy.this_monster["type"] + " hit points remaining: " + str(enemy.this_monster["hp"]))

    if enemy.this_monster["hp"] < 1:
        time.sleep(1)
        print("You have defeated the " + enemy.this_monster["type"] + "!")
        xp_earned = enemy.this_monster["xp"]
        character["xp"] = character["xp"] + xp_earned
    else: 
        time.sleep(1)
        print("You have failed at level" + character["lvl"] + ", better luck next time!")
        exit()

    if character["xp"] >= (character["lvl"] * 20):
        character["lvl"] = character["lvl"] + 1
        character["xp"] = 0
        print("Congratulations " + character["charname"] + " you have cleared this level, and may ascend up to Floor " + str(character["lvl"]) + "!")
    else:
        time.sleep(2)
        print("You must defeat more enemies to advance.")
        time.sleep(1)
        encounter()

encounter()
    