from battle import pilihMonster, showStat, banyakMonster, check
from potion import getPotion, potionStatus, potionList
from load import load, loadInvent, showDict
from monster import level, get_stats
from share import display, sleep, clear, pilihanValid, displayBar, maxEle, minEle
from rng import random

def arena(dataUser:dict, potionUser:dict, monsterUser:dict):
    clear()
    statAgent = enterArena(dataUser, monsterUser)
    hasilLatihan = {
        "Total Hadiah": 0,
        "Jumlah Stage": 0,
        "Damage diberikan": 0,
        "Damage diterima": 0,
        "Potion digunakan": 0,
        "Total turn": 0,
        "Battle terlama": 0,
        "Battle tersingkat": 0
    }
    dataRonde = []
    dataPotion = potionStatus(potionUser)
    for i in range(1,6):
        print(f"Memasuki Ronde {i}...")
        sleep(3)
        [isMenang, kondisi] = battleArena(potionUser, statAgent, i, hasilLatihan, dataRonde, dataPotion, dataUser)
        if isMenang:
            continue
        else:
            sleep(3)
            break
    hasilLatihan["Potion digunakan"] = dataPotion["Strength"] + dataPotion["Resilience"] + dataPotion["Healing"]
    hasilLatihan["Battle terlama"] = maxEle(dataRonde)
    hasilLatihan["Battle tersingkat"] = minEle(dataRonde)
    if kondisi == 1:
        display("GAME OVER !, Anda mengakhiri battle")
        showDict(hasilLatihan)
        return isMenang
    elif kondisi == 2:
        display("GAME OVER !, Anda kalah")
        showDict(hasilLatihan)
        return isMenang
    elif kondisi == 3:
        display("CONGRATS !, Anda menang ")
        showDict(hasilLatihan)
        return isMenang
    return True

def enterArena(dataUser:dict, monsterUser:dict) ->dict:
    namaUser = dataUser["Username"]
    userId = dataUser["ID"]
    display("Selamat datang di Arena !!! ")
    monsterId = pilihMonster(userId, withList=True)
    levelMonster = level(monsterId, monsterUser)
    statAgent = get_stats(monsterId, levelMonster)
    print(
r"""
  _,-""`""-~`)
(`~_,=========\
 |---,___.-.__,\
 |        o     \ ___  _,,,,_     _.--.
  \      `^`    /`_.-"~      `~-;`     \
   \_      _  .'                 `,     |
     |`-                           \'__/ 
    /                      ,_       \  `'-. 
   /    .-""~~--.            `"-,   ;_    /
  |              \               \  | `""`
   \__.--'`"-.   /_               |'
              `"`  `~~~---..,     |
                             \ _.-'`-.
                              \       \
                               '.     /
                                 `"~"`""")
    print(f"RAWRR, Agent {namaUser} mengeluarkan monster {statAgent["Name"]} !!!")
    showStat(statAgent)
    return statAgent

def battleArena(potionUser:dict, statAgent:dict, arena:int,  hasilLatihan:dict, dataRonde:list, dataPotion:dict, dataUser:dict) -> bool:
    clear()
    dataHadiah = [30, 50, 100, 200, 400]
    kondisi = 0
    idMusuh = random(numRange=[1, banyakMonster()])
    levelMusuh = arena
    statMusuh = get_stats(idMusuh, levelMusuh)
    print(
r"""           _.------.                        .----.__
           /         \_.       ._           /---.__  \
          |  O    O   |\\___  //|          /       `\ |
          |  .vvvvv.  | )   `(/ |         | o     o  \|
          /  |     |  |/      \ |  /|   ./| .vvvvv.  |\
         /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \
       ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/\\
      /   / |         \        /  | | ~   \          |  \\
      \  /  |        / \ Y   /'   | \     |          |   ~
       `'   |  _     |  `._/' |   |  \     7        /
         _.-'-' `-'-'|  |`-._/   /    \ _ /    .    |
    __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_
 --'                  \  \ |   /    |  |              `-
                       \uU \UU/     |  /   :F_P:""")
    print(f"RAWRR, Monster {statMusuh["Name"]} telah muncul !!!") 
    sleep(3)
    ronde:int = 0
    status = potionStatus(potionUser)
    maxHpMusuh = statMusuh["HP"]
    maxHpAgent = statAgent["HP"]
    levelMusuh = statMusuh["Level"]
    clear()
    while kondisi == 0:
        ronde += 1
        isEscape = turnArena(hasilLatihan, dataPotion, ronde, statAgent, statMusuh, status, potionUser, maxHpMusuh, maxHpAgent)
        [hasil, kondisi] = check(isEscape, statAgent, statMusuh)
        if kondisi != 0:
            break
        turnMusuhArena(hasilLatihan, ronde, statAgent, statMusuh)
        [hasil, kondisi] = check(isEscape, statAgent, statMusuh)
    clear()
    if kondisi == 3:
        hadiah = dataHadiah[arena-1]
        hasilLatihan["Total Hadiah"] += hadiah
        hasilLatihan["Total turn"] += ronde
        hasilLatihan["Jumlah Stage"] = arena
        dataRonde.append(ronde)
        dataUser["OC"] = str(int(dataUser["OC"]) + hadiah)
        display(f"Selamat anda telah menyelesaikan ronde {arena}, mendapatkan {hadiah} OC !!!")
    sleep(3)
    return [hasil, kondisi]

def turnArena(hasilLatihan:dict, dataPotion, number:int, allies:dict, enemies:dict, status:list, potionUser:dict, maxHpMusuh:int, maxHpAgent:int) -> bool:
    while True:
        clear()
        showStat(enemies, maxHpMusuh)
        print("                                         VS                                         ")
        showStat(allies, maxHpAgent)
        displayBar(f"Turn {number} ({allies["Name"]})")
        print(
f"""1. Attack
2. Use Potion
3. Escape""")
        pilihan =int(pilihanValid(input("<///> Pilih perintah: "), ["1", "2", "3"]))
        if pilihan == 1:
            dmg = attackArena(allies["Atk"], enemies["Def"], allies["Name"], enemies["Name"], enemies)
            hasilLatihan["Damage diberikan"] += dmg
            return False
        elif pilihan == 2:
            maxPilihan = potionList(potionUser)
            isCancel = usePotionArena(status, dataPotion, potionUser, maxPilihan, allies, maxHpAgent)
            if isCancel:
                continue
            return False
        else:
            return True

def turnMusuhArena(hasilLatihan:dict, number:int, allies:dict, enemies:dict):
    displayBar(f"Turn {number} ({enemies["Name"]})")
    dmg = attackArena(enemies["Atk"], allies["Def"], enemies["Name"], allies["Name"], allies)
    hasilLatihan["Damage diterima"] += dmg
    clear()

def attackArena(Atk:int, Def:int, attackerName:str, defenderName:str, defender:list):
    lowATK = int(Atk * 7/10)
    highATK = int(Atk * 13/10)
    rngATK = random(numRange=[lowATK, highATK])
    DEF = rngATK * (Def/100)
    damage = int(rngATK - DEF)
    print(f"{attackerName} attack {defenderName} dealing {damage} damage !!!")
    defender["HP"] -= damage
    if defender["HP"] < 0:
        defender["HP"] = 0
    sleep(3)
    return damage

def usePotionArena(status:list, dataPotion:dict, potionUser:dict, maxPilihan:int, allies:dict, maxHp:int):
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih potion: "), [str(i+1) for i in range(maxPilihan)]))
        if pilihan-1 == len(status):
            clear()
            return True
        typePotion = [potion for potion in potionUser][pilihan-1]
        quantity = int(potionUser[typePotion])
        if quantity == 0:
            print(f"{typePotion} potion sudah habis")
        elif status[typePotion] == "1":
            print("sudah digunakan")
        else:
            print(f"{typePotion} potion digunakan")
            dataPotion
            quantity -= 1
            potionUser[typePotion] = str(quantity)
            if typePotion == "Strength":
                allies["Atk"] += int(5 / 100 * allies["Atk"])
            elif typePotion == "Resilience":
                allies["Def"] += int(5 / 100 * allies["Def"])
            elif typePotion == "Healing":
                allies["HP"] += int(25 / 100 * maxHp)
                if allies["HP"] > maxHp:
                    allies["HP"] = maxHp
            status[typePotion] = str(1)
            dataPotion[typePotion] += 1
            sleep(2)
            return False

if __name__ == "__main__":
    userId = 3
    potionUser = getPotion(userId)
    dataUser = load("user", userId)
    monsterUser = loadInvent(userId, "monster")
    arena(dataUser, potionUser, monsterUser)