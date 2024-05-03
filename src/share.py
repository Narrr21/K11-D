import os

class YesOrNo:
    def __init__(self, masukan:str) -> str:
        while True:
            if masukan != "Y" and masukan != "N":
                print("Masukan yang valid hanya Y atau N")
                masukan = input("<///> Y/N: ")
                os.system('cls')
            else:
                break
        self.YN = masukan

def get_stats(id:int, level:int) -> dict:
    stat = {
        "Name": statMonster(id, 1),
        "Atk": int(statMonster(id, 2)),
        "Def": int(statMonster(id, 3)),
        "Hp": int(statMonster(id, 4)),
        "Level": level
    }
    return stat


def display(text:str):
    print(f"""
<==================================================================================>
{text}
<==================================================================================>""")

def pilihMonster(userId:int, withList:bool=False) -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    data = monsterInventory()
    hasil = search(0, str(userId), data)
    if withList:
        print("<============> MONSTER LIST <============>")
        for i in range(len(hasil)):
            monsterId = int(hasil[i][1])
            print(f"{i+1}. {statMonster(monsterId, 1)}")
    while True:
        pilihan = int(input("<///> Pilih monster: "))
        os.system('cls')
        if 0 < pilihan < len(hasil)+1:
            return hasil[pilihan-1][1]
        else:
            print("pilihan tidak tersedia!")

def split(baris:str, pemisah:str=None) -> list:
    if pemisah is None:
        pemisah = " "
    hasil = []
    temp = ""
    for char in baris:
        if char != pemisah:
            temp += char
        else:
            hasil.append(temp)
            temp = ""
    hasil.append(temp[:-1])
    return hasil

def splitcsv(file:list) -> list:
    hasil:list = []
    for line in file:
        row = list(split(line, ";"))
        hasil.append(row)
    return hasil

def monsterInventory() -> list:
    with open(r'data\monster_inventory.csv', 'r') as file:
        return splitcsv(file)

def dataMonster() -> list:
    with open(r'data\monster.csv', 'r') as file:
        return splitcsv(file)

def statMonster(monsterId:int, statIndex:int):
    data = dataMonster()
    hasil = search(0, str(monsterId), data)
    return hasil[0][statIndex]

def monsterList(userId:int) -> list:
    data = monsterInventory()
    hasil = search(0, str(userId), data)
    print("<============> MONSTER LIST <============>")
    for i in range(len(hasil)):
        monsterId = int(hasil[i][1])
        print(f"{i+1}. {statMonster(monsterId, 1)}")

def search(searchIndex:int, searchInput:str, file:list) -> list:
    hasil = []
    for row in file:
        if searchInput == row[searchIndex]:
            hasil.append(row)
    return hasil
def level(userId:int, monsterId:int):
    data = monsterInventory()
    dataUser = search(0, str(userId), data)
    hasil = search(1, str(monsterId), dataUser)
    return int(hasil[0][2])

