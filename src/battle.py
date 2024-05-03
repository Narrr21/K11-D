import os
import time
from rng import random
from share import pilihMonster, level, get_stats,display

def battle() -> bool:
    dataBattle = encounter()
    statAgent:dict = dataBattle[0]
    statMusuh:dict = dataBattle[1]
    ronde:int = 0
    os.system("cls")
    while True:
        ronde += 1
        showStat(statMusuh)
        showStat(statAgent)
        turn(ronde, statAgent, statMusuh)
        showStat(statMusuh)
        showStat(statAgent)
        turn(ronde, statMusuh, statAgent, agent=False)
        check()

def encounter() -> list:
    statMusuh = musuh()
    print(f"RAWRR, Monster {statMusuh["Name"]} telah muncul !!!")
    showStat(statMusuh)
    userId = 3 #Placeholder
    namaUser = "x" #placeholder
    monsterId = pilihMonster(userId, withList=True)
    levelMonster = level(userId, monsterId)
    statAgent = get_stats(monsterId, levelMonster)
    print(f"RAWRR, Agent {namaUser} mengeluarkan monster {statAgent["Name"]} !!!")
    showStat(statAgent)
    print("Entering Battle...")
    time.sleep(2)
    return [statAgent, statMusuh]

def musuh()-> dict:
    idMusuh = random.generate((1,5))
    levelMusuh = random.generate((1,5))
    statMusuh = get_stats(idMusuh, levelMusuh)
    return statMusuh

def showStat(stat:dict) -> str:
    display (
f"""Name      : {stat["Name"]}
ATK Power : {stat["Atk"]}
DEF Power : {stat["Def"]}
HP        : {stat["Hp"]}
Level      : {stat["Level"]}""")

def turn(number:int, allies:dict, enemies:dict, agent:bool=True):
    if agent:
        print(
f"""
<============> Turn {number} ({allies["Name"]}) <============>
1. Attack
2. Use Potion
3. Quit
""")
        pilihan = int(input("<///> Pilih perintah: "))
        while True:
            if pilihan in [1, 2, 3]:
                if pilihan == 1:
                    attack(allies["Atk"], enemies["Def"], allies, enemies)
                    break
                else:
                    break
            else:
                print("pilihan tidak tersedia!")
    else:
        attack(allies["Atk"], enemies["Def"], allies, enemies)
    os.system("cls")

def attack(Atk:int, Def:int, allies:dict, enemies:dict):
    lowATK = int(Atk * 7/10)
    highATK = int(Atk * 13/10)
    rngATK = random.generate((lowATK, highATK))
    DEF = rngATK * (Def/100)
    damage = int(rngATK - DEF)
    print(f"{allies["Name"]} attack {enemies["Name"]} dealing {damage} damage !!!")
    time.sleep(4)

def check():
    ...

battle()