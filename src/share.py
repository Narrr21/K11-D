import os
import time

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

def display(text:str):
    print(f"""<==================================================================================>
{text}
<==================================================================================>""")

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

def sleep(waktu:int=2):
    time.sleep(waktu)

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
