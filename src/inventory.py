from battle import showStat
from share import clear, display, pilihanValid, readcsv, search, level, YesOrNo
from monster import get_stats, getMonsterUser
from potion import getPotionUser

def inventory(userId:int):
    while True:
        clear()
        dataMonster = monsterInventory(userId)
        inventMonsterUser = dataMonster[0]
        dataStatMonster = dataMonster[1]

        dataPotion = potionInventory(userId)
        inventPotionUser = dataPotion[0]
        dataStatPotion = dataPotion[1]
        
        # penggabungan list monster dan potion
        for i in inventPotionUser:
            inventMonsterUser.append(i)
        invent = inventMonsterUser

        # Menampilkan hasil ke terminal
        print(f"<=========> Inventory List (User ID : {userId})<==========>")
        for barang in enumerate(invent):
            print(f"{barang[0]+1}. {barang[1]}")
        nomor = len(invent)
        print("Ketikkan id untuk menampilkan item")
        pilihan = pilihanValid(input("<///> : "), [str(i) for i in range(1, nomor+1)])
        if pilihan in range(1, nomor+1):
            clear()
            if invent[pilihan-1][:7] == "Monster":
                print("Monster")
                showStat(dataStatMonster[pilihan-1])
            elif invent[pilihan-1][:6] == "Potion":
                data = dataStatPotion[pilihan - len(dataStatMonster) - 1]
                print("Potion")
                display(
f"""Type     : {data[0]}
Quantity : {data[1]}""")
        isExit = YesOrNo(input("<///> Keluar (Y/N): "))
        if isExit:
            break

def monsterInventory(userId:int):
    # memanggil data monster, monster_inventory dan mencari user yang sesuai
    dataMonster = readcsv("monster")
    monsterUser = getMonsterUser(userId)
    inventMonsterUser = []
    dataStatMonster = []

    # mwmbuat data string monster dan data stat
    for monster in monsterUser:
        monsterId:int = int(monster[1])
        dataMonsterUser = search(0, str(monsterId), dataMonster)
        namaMonster = dataMonsterUser[0][1]
        levelMonster = level(userId, monsterId)
        maxHp = dataMonsterUser[0][4]
        hasil = "Monster" + " " * (15- len("Monster")) + f"(Name: {namaMonster}, Lvl: {levelMonster}, HP: {maxHp})"
        inventMonsterUser.append(hasil)
        stat = get_stats(monsterId, levelMonster)
        dataStatMonster.append(stat)    
    return [inventMonsterUser, dataStatMonster]

def potionInventory(userId:int):
    potionUser = getPotionUser(userId)
    inventPotionUser = []
    dataPotion = []
    # membuat data string potion dan data potion
    for potionType in potionUser:
        if potionType == "Strength":
            type = "ATK"
        elif potionType == "Resilience":
            type = "DEF"
        elif potionType == "Healing":
            type = "Heal"
        quantity = potionUser[potionType]
        hasil:str = "Potion" + " " * (15- len("Potion")) + f"(Type: {type}, Qty: {quantity})"
        dataPotion.append([type, quantity])
        inventPotionUser.append(hasil)
    return [inventPotionUser, dataPotion]

inventory(3)