from share import readcsv, search, pilihanValid, clear

def statMonster(monsterId:int, statIndex:int):
    data = readcsv("monster")
    hasil = search(0, str(monsterId), data)
    return hasil[0][statIndex]

def monsterList(userId:int) -> list:
    data = readcsv("monster_inventory")
    hasil = search(0, str(userId), data)
    print("<============> MONSTER LIST <============>")
    for [i,j] in enumerate(hasil):
        monsterId = int(j[1])
        print(f"{i+1}. {statMonster(monsterId, 1)}")

def get_stats(id:int, level:int) -> dict:
    if level == 1:
        pengaliLevel = 1
    else:
        pengaliLevel = ((level - 1) * 10 + 100) / 100
    stat = {
        "Name": statMonster(id, 1),
        "Atk": int(int(statMonster(id, 2)) * pengaliLevel),
        "Def": int(int(statMonster(id, 3)) * pengaliLevel),
        "Hp": int(int(statMonster(id, 4)) * pengaliLevel),
        "Level": level
    }
    return stat

def pilihMonster(userId:int, withList:bool=False) -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    data = readcsv("monster_inventory")
    hasil = search(0, str(userId), data)
    if withList:
        monsterList(userId)
    while True:
        pilihan = pilihanValid(input("<///> Pilih monster: "), [f'{i+1}' for i in range(len(data))])
        clear()
        if 0 < pilihan < len(hasil)+1:
            return hasil[pilihan-1][1]
        else:
            print("pilihan tidak tersedia!")

def getMonsterUser(userId:int):
    inventMonster = readcsv("monster_inventory")
    monsterUser = search(0, str(userId), inventMonster)
    return monsterUser