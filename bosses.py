import random

class boss():
    boss = {"name": "", "type": "", "hp": 0, "attack": "", "dmg": 0}

    boss_types = ["Dragon"]

    boss["type"] = random.choice(boss_types)

    if boss["type"] == "Dragon":
        boss = {"name": "", "type": "Dragon", "hp": 20, "attack": "scorches", "dmg": 5}
        dragon_names = ["Drakaroth", "Sylvestra", "Auronex", "Virelith", "Zephyrion", "Nivalis", "Seraphira", "Nocturnis", "Verdantix", "Celestrix", "Solarius", 
                "Pyralis", "Tyranthor", "Lumidra", "Infernix", "Aquavox", "Jormungandr", "Nidhogg", "Fafnir", "Midgardsormr", "Lyngbakr", "Nafnafell", 
                "Hafgufa", "Otr", "Fjalar", "Jǫrmungandr", "Elivagar"]
        boss["name"] = random.choice(dragon_names)