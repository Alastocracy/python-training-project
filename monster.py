#pick a random low level monster
class monster():
  monster_list = [
    {"type": "Giant Rat", "hp": 10, "attack": "bites", "dmg": 1, "xp": 2},
    {"type": "Goblin", "hp": 10,"attack": "stabs", "dmg": 1, "xp": 10},
    {"type": "Orc", "hp": 15, "attack": "slashes","dmg": 2, "xp": 15},
    {"type": "Hobgoblin", "hp": 20, "attack": "smashes", "dmg": 2, "xp": 20}
    ]

#pick a random mid level monster
class bigger_monster():
  monster_list = [
    {"type": "Hobgoblin", "hp": 20, "attack": "smashes", "dmg": 2, "xp": 20},
    {"type": "Swarm of Rats", "hp": 40, "attack": "smashes", "dmg": 1, "xp": 20},
    {"type": "Wolf", "hp": 20, "attack": "bites", "dmg": 4, "xp": 40},
    {"type": "Skeletal Swordsman", "hp": 40, "attack": "slashes", "dmg": 2, "xp": 40}
  ]

#pick a high level monster
class biggest_monster():
  monster_list = [
    {"type": "Skeletal Swordsman", "hp": 40, "attack": "slashes", "dmg": 2, "xp": 40},
    {"type": "Death Knight", "hp": 60, "attack": "strikes", "dmg": 5, "xp": 60},
    {"type": "Ghoul", "hp": 60, "attack": "curses", "dmg": 1, "xp": 50},
    {"type": "Warlock", "hp": 30, "attack": "zaps", "dmg": 10, "xp": 60},
  ]
