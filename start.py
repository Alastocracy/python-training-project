import random
import time
import os
from monsters import monster
from monsters import bigger_monster
from monsters import biggest_monster
from bosses import boss

#encounter function to pick enemies based on char level
def encounter():
    #declare enemy as null when class is called to not use the same monster stats
    enemy = {}
    if character["lvl"] < 3:
        monster()
        enemy = random.choice(monster.monster_list)
    elif character["lvl"] < 5:
        bigger_monster()
        enemy = random.choice(bigger_monster.monster_list)
    elif character["lvl"] < 7:
        enemy = random.choice(biggest_monster.monster_list)
    
    print("From the darkness a foe approaches...")
    time.sleep(2)
    print("A " + enemy["type"] + " appears!")

    #fight sequence
    while enemy["hp"] > 0 and character["hp"] > 0:
        time.sleep(1)
        character["hp"] = character["hp"] - enemy["dmg"]
        print("The " + enemy["type"] + " " + enemy["attack"] + " you for " + str(enemy["dmg"]) +" damage.")
        time.sleep(1)
        enemy["hp"] = enemy["hp"] - character["dmg"]
        print("You strike the " + enemy["type"] + " back for " + str(character["dmg"]) + " damage.")
        time.sleep(1)
        print(character["charname"] + " hit points remaining: " + str(character["hp"]) + ", " + enemy["type"] + " hit points remaining: " + str(enemy["hp"]))

    #combat clean up
    if enemy["hp"] < 1:
        time.sleep(1)
        print("You have defeated the " + enemy["type"] + "!")
        xp_earned = enemy["xp"]
        character["xp"] = character["xp"] + xp_earned
    else: 
        time.sleep(1)
        print("Oof, thats unlucky. You have failed at level " + str(character["lvl"]) + ", better luck next time!")
        exit()

    #level up and next level
    if character["xp"] >= (character["lvl"] * 20):
        character["lvl"] = character["lvl"] + 1
        character["xp"] = 0
        character["hp"] = character["lvl"] * 30
        character["dmg"] = character["lvl"] * 2
        print("As the last enemy in the chamber falls, a warmth fills you.\nYou feel refreshed, and perhaps even stronger than before.")
        time.sleep(1)
        print("Congratulations " + character["charname"] + " you have cleared this level, and may ascend up to Floor " + str(character["lvl"]) + "!")
        time.sleep(2)
        os.system('cls')
    else:
        time.sleep(2)
        os.system('cls')
        print("You must defeat more enemies to advance to the next level.")
        time.sleep(1)
        encounter()

#Function for tower floor loop
def floor():
    os.system('cls')
    time.sleep(2)
    print("FLOOR " + str(character["lvl"]))
    time.sleep(2)
    encounter()

def boss_floor():
    os.system('cls')
    time.sleep(2)
    print("FLOOR " + str(character["lvl"]))
    time.sleep(2)

    enemy = {}
    boss()
    enemy = boss.boss
    enemy["dmg"] = enemy["dmg"] * character["lvl"]
    enemy["hp"] = enemy["hp"] * character["lvl"]

    print("The chamber lights up, illuminating a new enemy across the chamber.")
    time.sleep(2)
    print("Greetings " + character["charname"] + ", I am " + enemy["name"] + " the " + enemy["type"] + " and your time in The Tower is at an end")

    while enemy["hp"] > 0 and character["hp"] > 0:
        time.sleep(1)
        character["hp"] = character["hp"] - enemy["dmg"]
        print("The " + enemy["type"] + " " + enemy["attack"] + " you for " + str(enemy["dmg"]) +" damage.")
        time.sleep(1)
        enemy["hp"] = enemy["hp"] - character["dmg"]
        print("You strike the " + enemy["type"] + " back for " + str(character["dmg"]) + " damage.")
        time.sleep(1)
        print(character["charname"] + " hit points remaining: " + str(character["hp"]) + ", " + enemy["type"] + " hit points remaining: " + str(enemy["hp"]))

    #combat clean up
    if enemy["hp"] < 1:
        time.sleep(1)
        print("You have defeated " + enemy["name"] + " the " + enemy["type"] + "!")
    else: 
        time.sleep(1)
        print("Oof, thats unlucky. You have failed at level " + str(character["lvl"]) + ", better luck next time!")
        exit()
    #levevl up after defeating the boss
    character["lvl"] = character["lvl"] + 1
    character["xp"] = 0
    character["hp"] = character["lvl"] * 30
    character["dmg"] = character["lvl"] * 2
    time.sleep(1)
    print("Congratulations " + character["charname"] + " you have cleared this level, and may ascend up to Floor " + str(character["lvl"]) + "!")
    
#THE GAME

#Clear terminal at start
os.system('cls')

#Intro
name = input("Hello Adventurer, what is your name? ")

#Create starting character template
character = {
    "charname": name,
    "lvl": 1,
    "xp": 0,
    "hp": 30,
    "dmg": 2,
}

#Explain the game
time.sleep(2)
print("Well met " + character["charname"] + " , welcome to The Tower.")
time.sleep(2)
print("Once you have vanquished the foes on this level, you will proceed to the one above.")
time.sleep(2)
print("Fight your way to the top to be crowned Tower Champion.\nGood luck!")
time.sleep(2)
print("Fade to black...")
time.sleep(4)

#Level 1-6 game loop
floor()
floor()
floor()
floor()
floor()
floor()
boss_floor()
boss_floor()