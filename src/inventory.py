from battle import showStat
from share import clear, display, pilihanValid, YesOrNo, displayBar
from monster import get_stats, level
from potion import getPotion
from load import getDataUser, loadInvent


def inventory(dataUser, monsterUser, potionUser):
    while True: 
        clear()
        [inventMonsterUser, dataStatMonster] = monsterInventory(monsterUser)
        [inventPotionUser, dataStatPotion] = potionInventory(potionUser)
        # penggabungan list monster dan potion
        for i in inventPotionUser:
            inventMonsterUser.append(i)
        invent = inventMonsterUser
        # Menampilkan hasil ke terminal
        displayBar("User Info")
        print(
f"""User ID : {dataUser["ID"]}
Nama    : {dataUser["Username"]}
OC      : {dataUser["OC"]}""")
        displayBar("Inventory List")
        for barang in enumerate(invent):
            print(f"{barang[0]+1}. {barang[1]}")
        nomor = len(invent) + 1
        print(f"{nomor}. Keluar")
        print("Ketikkan id untuk menampilkan item")
        pilihan = int(pilihanValid(input("<///> : "), [str(i) for i in range(1, nomor+1)]))
        clear()
        if pilihan == nomor:
            break
        elif invent[pilihan-1][:7] == "Monster":
            print("Monster")
            showStat(dataStatMonster[pilihan-1])
        elif invent[pilihan-1][:6] == "Potion":
            data = dataStatPotion[pilihan - len(dataStatMonster) - 1]
            print("Potion")
            display(
f"""Type     : {data[0]}
Quantity : {data[1]}""")
        isExit = YesOrNo(input("<///> Keluar Inventory (Y/N): "))
        if isExit:
            break

def monsterInventory(monsterUser:dict):
    # memanggil data monster, monster_inventory dan mencari user yang sesuai
    desc = []
    dataStatMonster = []
    # mwmbuat data string monster dan data stat
    for monster in monsterUser["MonsterID"]:
        monsterId:int = int(monster)
        levelMonster = level(monsterId, monsterUser)
        stat = get_stats(monsterId, levelMonster)
        maxHp = stat["HP"]
        namaMonster = stat["Name"]
        hasil = "Monster" + " " * (15- len("Monster")) + f"(Name: {namaMonster}, Lvl: {levelMonster}, HP: {maxHp})"
        desc.append(hasil)
        dataStatMonster.append(stat)    
    return [desc, dataStatMonster]

def potionInventory(potionUser:dict):
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

if __name__ == "__main__":
    userId = 3
    dataPotion = getPotion(userId)
    dataUser = getDataUser(userId) #Placeholder
    monsterUser = loadInvent(userId, "monster") #Placeholder
    inventory(dataUser, monsterUser, dataPotion)