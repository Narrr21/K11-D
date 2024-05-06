import os

def YesOrNo(masukan:str) -> str:
    masukan = str.upper(masukan)
    while True:
        if masukan != "Y" and masukan != "N":
            print("Masukan yang valid hanya Y atau N")
            masukan = input("<///> Y/N: ")
        else:
            return masukan == "Y"

def pilihanValid(masukan:str, validRange:list[str]) -> int:
    while True:
        if masukan in validRange:
            return int(masukan)
        else:
            print("Masukan tidak valid")
            masukan = input("<///> Pilih perintah: ")

def isDigit(masukan:str) -> int:
    while True:
        valid = False
        for char in masukan:
            if 48 <= ord(char) <= 57:
                valid = True
            else:
                valid = False
                print("Masukkan input bertipe Integer, coba lagi!")
                masukan = input("<///> Masukan : ")
                break
        if valid:
            return int(masukan)


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


def display(text:str):
    print(f"""<==================================================================================>
{text}
<==================================================================================>""")

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

def readcsv(fileName:str) -> list[list[str]]:
    with open(f'data\{fileName}.csv', 'r') as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        return hasil

def clear():
    os.system("cls")

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

def potionList(userId:int) -> int:
    data = readcsv("item_inventory")
    hasil = search(0, str(userId), data)
    print("<============> POTION LIST <============>")
    for [i, potion] in enumerate(hasil):
        print(f"{i+1}. {potion[1]} Potion (Qty: {potion[2]})", end="")
        if potion[1] == "strength":
            print(" - Increase ATK Power")
        elif potion[1] == "resilience":
            print(" - Increase DEF Power")
        elif potion[1] == "healing":
            print(" - Restore Health")
        else: 
            print()
    print(f"{i+2}. Cancel")
    return i

def search(searchIndex:int, searchInput:str, file:list) -> list:
    hasil = []
    for row in file:
        if searchInput == row[searchIndex]:
            hasil.append(row)
    return hasil
def level(userId:int, monsterId:int):
    data = readcsv("monster_inventory")
    dataUser = search(0, str(userId), data)
    hasil = search(1, str(monsterId), dataUser)
    return int(hasil[0][2])
