import os
from rng import random
from share import display,pilihMonster

def battle():
    idMusuh = random.generate((1,5))
    statMusuh = {
        "Name" : "Zuko", #placeholder
        "ATK Power" : 20, #placeholder
        "DEF Power" : 20, #placeholder
        "HP" : 100, #placeholder
        "Level" : 1 #placeholder
    }
    print("Monster List") #placeholder
    mosnterId = pilihMonster()
    statMonster = {
        "Name" : "Pikachow", #placeholder
        "ATK Power" : 25, #placeholder
        "DEF Power" : 5, #placeholder
        "HP" : 120, #placeholder
        "Level" : 1 #placeholder
    }

battle()