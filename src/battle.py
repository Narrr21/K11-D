from rng import random
from share import display, clear, pilihanValid, sleep, displayBar
from monster import get_stats, pilihMonster, level, banyakMonster
from potion import potionStatus, potionList, getPotion
from load import loadInvent, load

def battle(dataUser:dict, potionUser:dict, arena:int=None) -> bool:
    clear()
    hasil = 0
    userId = dataUser["ID"]
    namaUser = dataUser["Username"]
    if arena is None:
        [statAgent, statMusuh] = encounter(userId, namaUser)
    else:
        [statAgent, statMusuh] = encounter(userId, namaUser, arena)
    ronde:int = 0
    status = potionStatus(potionUser)
    maxHpMusuh = statMusuh["HP"]
    maxHpAgent = statAgent["HP"]
    clear()
    while hasil == 0:
        ronde += 1
        isEscape = turn(ronde, statAgent, statMusuh, status, potionUser, maxHpMusuh, maxHpAgent)
        hasil = check(isEscape, statAgent, statMusuh)
        if hasil != 0:
            break
        turn(ronde, statAgent, statMusuh, status, potionUser, maxHpMusuh, maxHpAgent, agent=False)
        hasil = check(isEscape, statAgent, statMusuh)
    clear()
    showStat(statMusuh, maxHpMusuh)
    print("                                         VS                                         ")
    showStat(statAgent, maxHpAgent)
    if hasil == 1:
        display("Anda berhasil kabur dari Battle!")
        return False
    elif hasil == 2:
        display("Sayang sekali anda kalah")
        print(
r"""        `;-.          ___,
          `.`\_...._/`.-"`
            \        /      ,
            /()   () \    .' `-._
           |)  .    ()\  /   _.'
           \  -'-     ,; '. <
            ;.__     ,;|   > \
           / ,    / ,  |.-'.-'
          (_/    (_/ ,;|.<`
            \    ,     ;-`
             >   \    /
            (_,-'`> .'
                 (_,'""")
        return False
    elif hasil == 3:
        dataUser["OC"] += random(numRange=[20, 50])
        display("Selamat anda menang")
        print(
r"""                                ___.
                                L._, \\
               _.,             <  <\\                _
             ,' '              `.   | \\            ( `
          ../, `.               |    .\\`.           \\ \\_
         ,' ,..  .           _.,'    ||\\l            )  '\".
        , ,'   \\           ,'.-.`-._,'  |           .  _._`.
      ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\
    .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-\"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
 / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.
.  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\
' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`
|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `\".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \\-.._,.'/'
          .     /        .               .       \\    .''
        .`.    |         `.             /         :_,'.'
          \\ `...\\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /\"'          |  \"'   '_
               /_|.-'\\ ,\".             '.'`__'-( \\
                 / ,\"'\"\\,'               `/  `-.|\"""")
        return True
    

def encounter(userId:int, namaUser:str, arena:int=None) -> list:
    idMusuh = random(numRange=[1, banyakMonster()])
    if arena is None:
        levelMusuh = random(numRange=[1,5])
    else:
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
    showStat(statMusuh)
    monsterId = pilihMonster(userId, withList=True)
    statUser = loadInvent(userId, "monster")
    levelMonster = level(monsterId, statUser)
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
    print("Entering Battle...")
    sleep(3)
    return [statAgent, statMusuh]

def showStat(stat:dict, maxHp:int=None) -> str:
    if maxHp is None:
        maxHp = stat["HP"]
    display (
f"""Name      : {stat["Name"]}
ATK Power : {stat["Atk"]}
DEF Power : {stat["Def"]}
HP        : {stat["HP"]}/{maxHp}
Level     : {stat["Level"]}""")

def turn(number:int, allies:dict, enemies:dict, status:list, potionUser:dict, maxHpMusuh:int, maxHpAgent:int, agent:bool=True) -> bool:
    if agent:
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
                attack(allies["Atk"], enemies["Def"], allies["Name"], enemies["Name"], enemies)
                return False
            elif pilihan == 2:
                maxPilihan = potionList(potionUser)
                isCancel = usePotion(status, potionUser, maxPilihan, allies, maxHpAgent)
                if isCancel:
                    continue
                return False
            else:
                return True
    else:
        displayBar(f"Turn {number} ({enemies["Name"]})")
        attack(enemies["Atk"], allies["Def"], enemies["Name"], allies["Name"], allies)
        clear()

def attack(Atk:int, Def:int, attackerName:str, defenderName:str, defender:list):
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

def usePotion(status:list, potionUser:dict, maxPilihan:int, allies:dict, maxHp:int):
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
            sleep(2)
            return False

def check(isEscape:bool, agent:dict, musuh:dict) -> int:
    if isEscape:
        return 1
    elif agent["HP"] == 0:
        return 2
    elif musuh["HP"] == 0:
        return 3
    else:
        return 0

if __name__ == "__main__":
    userId = 3
    potionUser = getPotion(userId)
    dataUser = load("user", userId)
    isMenang = battle(dataUser, potionUser)