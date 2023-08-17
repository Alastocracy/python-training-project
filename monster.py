import random

def monster():
    monster_list = [
        {"type": "giant rat", "hp": 10, "attack": "bites", "dmg": 1, "xp": 2},
        {"type": "goblin", "hp": 10,"attack": "stabs", "dmg": 1, "xp": 10},
        {"type": "orc", "hp": 15, "attack": "slashes","dmg": 2, "xp": 15},
        {"type": "hobgoblin", "hp": 20, "attack": "smashes", "dmg": 2, "xp": 20}
    ]
    
    this_monster = random.choice(monster_list)
