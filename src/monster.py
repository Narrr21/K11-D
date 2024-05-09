from share import arraycsv, search, pilihanValid, clear, index, displayBar
from load import load, loadInvent

def statMonster(monsterId:int, statIndex:int):
    data = arraycsv("monster")
    hasil = search(0, str(monsterId), data)
    return hasil[0][statIndex]

def get_stats(id:int, level:int) -> dict:
    if level == 1:
        pengaliLevel = 1
    else:
        pengaliLevel = ((level - 1) * 10 + 100) / 100
    stat = {
        "Name": statMonster(id, 1),
        "Atk": int(int(statMonster(id, 2)) * pengaliLevel),
        "Def": int(int(statMonster(id, 3)) * pengaliLevel),
        "HP": int(int(statMonster(id, 4)) * pengaliLevel),
        "Level": level
    }
    return stat

def monsterList(userId:int, data:dict=None) -> list:
    if data is None:
        data = loadInvent(userId, "monster")
    displayBar("MONSTER LIST")
    for element in enumerate(data["MonsterID"]):
        monsterID = element[1]
        levelMonster = level(monsterID, data)
        stat = get_stats(monsterID, levelMonster)
        monsterName = stat["Name"]
        monsterlist = f"{element[0]+1}. {monsterName}"
        space = 15 - len(monsterlist)
        print(monsterlist, " " * space + f"(Lvl: {levelMonster})")

def pilihMonster(userId:int, withList:bool=False) -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    data = arraycsv("monster_inventory")
    hasil = search(0, str(userId), data)
    if withList:
        monsterList(userId)
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih monster: "), [f'{i+1}' for i in range(len(data))]))
        clear()
        if 0 < pilihan < len(hasil)+1:
            return hasil[pilihan-1][1]
        else:
            print("pilihan tidak tersedia!")

def banyakMonster():
    return len(load("monster")["ID"])

def level(monsterId:int, data):
    hasil = data["Level"][index(str(monsterId), data["MonsterID"])]
    return int(hasil)

if __name__ == "__main__":
    monsterUser = loadInvent(3, "monster")