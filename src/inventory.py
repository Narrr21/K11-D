from battle import showStat
from share import clear, display, pilihanValid, readcsv, search, level, get_stats, YesOrNo

def inventory(userId:int):
    while True:
        clear()
        print(f"<=========> Inventory List (User ID : {userId})<==========>")
        inventMonster = readcsv("monster_inventory")
        dataMonster = readcsv("monster")
        monsterUser = search(0, str(userId), inventMonster)
        inventMonsterUser = []
        dataStatMonster = []
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
        inventPotion = readcsv("item_inventory")
        potionUser = search(0, str(userId), inventPotion)
        inventPotionUser = []
        dataPotion = []
        for potion in potionUser:
            potionType = potion[1]
            if potionType == "strength":
                type = "ATK"
            elif potionType == "resilience":
                type = "DEF"
            elif potionType == "healing":
                type = "Heal"
            dataPotion.append([type, potion[2]])
            hasil:str = "Potion" + " " * (15- len("Potion")) + f"(Type: {type}, Qty: {potion[2]})"
            inventPotionUser.append(hasil)
        for i in inventPotionUser[1:]:
            inventMonsterUser.append(i)
        invent = inventMonsterUser[1:]
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
                data = dataPotion[pilihan - len(dataStatMonster)]
                display(
f"""Potion
Type     : {data[0]}
Quantity : {data[1]}""")
        isExit = YesOrNo(input("<///> Keluar (Y/N): "))
        if isExit:
            break    