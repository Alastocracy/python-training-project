import random

#pick a random low level monster
class monster():
  monster_list = [
    {"type": "giant rat", "hp": 10, "attack": "bites", "dmg": 1, "xp": 2},
    {"type": "goblin", "hp": 10,"attack": "stabs", "dmg": 1, "xp": 10},
    {"type": "orc", "hp": 15, "attack": "slashes","dmg": 2, "xp": 15},
    {"type": "hobgoblin", "hp": 20, "attack": "smashes", "dmg": 2, "xp": 20}
    ]
  this_monster = random.choice(monster_list)

#pick a random mid level monster
class bigger_monster():
  monster_list = [
    {"type": "hobgoblin", "hp": 20, "attack": "smashes", "dmg": 2, "xp": 20},
    {"type": "swarm of rats", "hp": 40, "attack": "smashes", "dmg": 1, "xp": 20},
    {"type": "wolf", "hp": 20, "attack": "bites", "dmg": 4, "xp": 40},
    {"type": "skeletal swordsman", "hp": 40, "attack": "slashes", "dmg": 2, "xp": 40}
  ]
  this_monster = random.choice(monster_list)

#pick a high level monster
class biggest_monster():
  monster_list = [
    {"type": "skeletal swordsman", "hp": 40, "attack": "slashes", "dmg": 2, "xp": 40},
    {"type": "death knight", "hp": 60, "attack": "strikes", "dmg": 5, "xp": 60},
    {"type": "ghoul", "hp": 60, "attack": "curses", "dmg": 1, "xp": 50},
    {"type": "warlock", "hp": 30, "attack": "zaps", "dmg": 10, "xp": 60},
  ]
  this_monster = random.choice(monster_list)
