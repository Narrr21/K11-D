import os
import time
from rng import random
from share import pilihMonster, level, get_stats,display,potionList, potionStatus

def battle() -> bool:
    os.system("cls")
    hasil = 0
    userId = 3 #Placeholder
    namaUser = "x" #placeholder
    dataBattle = encounter(userId, namaUser)
    statAgent:dict = dataBattle[0]
    statMusuh:dict = dataBattle[1]
    ronde:int = 0
    status = potionStatus(userId)
    maxHpMusuh = statMusuh["Hp"]
    maxHpAgent = statAgent["Hp"]
    os.system("cls")
    while hasil == 0:
        ronde += 1
        isEscape = turn(ronde, userId, statAgent, statMusuh, status, maxHpMusuh, maxHpAgent)
        hasil = check(isEscape, statAgent, statMusuh)
        if hasil != 0:
            break
        turn(ronde, userId, statAgent, statMusuh, status, maxHpMusuh, maxHpAgent, agent=False)
        hasil = check(isEscape, statAgent, statMusuh)
    if hasil == 1:
        display("Anda berhasil kabur dari Battle!")
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
    elif hasil == 3:
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
    

def encounter(userId:int, namaUser:str) -> list:
    statMusuh = musuh()
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
    levelMonster = level(userId, monsterId)
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
    time.sleep(5)
    return [statAgent, statMusuh]

def musuh()-> dict:
    idMusuh = random.generate((1,5))
    levelMusuh = random.generate((1,5))
    statMusuh = get_stats(idMusuh, levelMusuh)
    return statMusuh

def showStat(stat:dict, maxHp:int=None) -> str:
    if maxHp is None:
        maxHp = stat["Hp"]
    display (
f"""Name      : {stat["Name"]}
ATK Power : {stat["Atk"]}
DEF Power : {stat["Def"]}
HP        : {stat["Hp"]}/{maxHp}
Level      : {stat["Level"]}""")

def turn(number:int, userId:int, allies:dict, enemies:dict, status:list, maxHpMusuh:int, maxHpAgent:int, agent:bool=True) -> bool:
    if agent:
        while True:
            showStat(enemies, maxHpMusuh)
            print("                                         VS                                         ")
            showStat(allies, maxHpAgent)
            print(
f"""<============> Turn {number} ({allies["Name"]}) <============>
1. Attack
2. Use Potion
3. Escape""")
            pilihan = int(input("<///> Pilih perintah: "))
            if pilihan in [1, 2, 3]:
                if pilihan == 1:
                    attack(allies["Atk"], enemies["Def"], allies["Name"], enemies["Name"], enemies)
                    os.system("cls")
                    return False
                elif pilihan == 2:
                    nomor = potionList(userId)
                    print(f"{nomor+1}. Cancel")
                    isCancel = usePotion(status, nomor, allies, maxHpAgent)
                    if isCancel:
                        continue
                    os.system("cls")
                    return False
                else:
                    os.system("cls")
                    return True
            else:
                print("pilihan tidak tersedia!")
    else:
        showStat(enemies, maxHpMusuh)
        print("                                         VS                                         ")
        showStat(allies, maxHpAgent)
        print(f"<============> Turn {number} ({enemies["Name"]}) <============>")
        attack(enemies["Atk"], allies["Def"], enemies["Name"], allies["Name"], allies)
        os.system("cls")

def attack(Atk:int, Def:int, attackerName:str, defenderName:str, defender:list):
    lowATK = int(Atk * 7/10)
    highATK = int(Atk * 13/10)
    rngATK = random.generate((lowATK, highATK))
    DEF = rngATK * (Def/100)
    damage = int(rngATK - DEF)
    print(f"{attackerName} attack {defenderName} dealing {damage} damage !!!")
    defender["Hp"] -= damage
    if defender["Hp"] < 0:
        defender["Hp"] = 0
    time.sleep(3)

def usePotion(status:list, number:int, allies:dict, maxHp:int):
    while True:
        pilihan = int(input("<///> Pilih potion: "))
        if pilihan in range(1, number+2):
            if pilihan-1 == len(status):
                os.system("cls")
                return True
            elif status[pilihan-1][1] == 1:
                print("sudah digunakan")
            else:
                print(f"{status[pilihan-1][0]} potion digunakan")
                #potion berkurang
                if status[pilihan-1][0] == "strength":
                    allies["Atk"] += int(5 / 100 * allies["Atk"])
                elif status[pilihan-1][0] == "resilience":
                    allies["Def"] += int(5 / 100 * allies["Def"])
                elif status[pilihan-1][0] == "healing":
                    allies["Hp"] += int(25 / 100 * maxHp)
                    if allies["Hp"] > maxHp:
                        allies["Hp"] = maxHp
                status[pilihan-1][1] = 1
                time.sleep(3)
                return False
        else:
            print("pilihan tidak tersedia!")

def check(isEscape:bool, agent:dict, musuh:dict) -> int:
    if isEscape:
        return 1
    elif agent["Hp"] == 0:
        return 2
    elif musuh["Hp"] == 0:
        return 3
    else:
        return 0
    

battle()