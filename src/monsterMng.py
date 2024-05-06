from share import pilihanValid, readcsv, YesOrNo, clear, display, isDigit
import time

def monsterManangement():
    while True:
        clear()
        print(
"""<===========================================>
SELAMAT DATANG DI DATABASE PARA MONSTER !!!
1. Tampilkan semua Monster
2. Tambah Monster Baru""")
        pilihan = pilihanValid(input("<///> Pilih perintah: "), ["1", "2"])
        if  pilihan in [1, 2]:
            data = dataMonsterManage()
            if pilihan == 1:
                showDict(data, columnLen=[2, 12, 10, 10, 6])
            else : # pilihan == 2
                newMonster = buatMonster(data)
                if newMonster[0]:
                    print("menambahkan ke database monster") #placeholder
                    ...
            isKeluar = YesOrNo(input("<///> Keluar (Y/N): "))
            if isKeluar:
                break
        else:
            print("Pilihan tidak tersedia")

def dataMonsterManage() -> dict:
    temp:list = readcsv("monster")
    monsterId:list = []
    monsterType:list = []
    monsterAtk:list = []
    monsterDef:list = []
    monsterHp:list = []
    data:dict = {
        "ID" : monsterId,
        "Type" : monsterType,
        "ATK Power" : monsterAtk,
        "DEF Power" : monsterDef,
        "HP" : monsterHp
    }
    for monster in temp[1:]:
        monsterId.append(int(monster[0]))
        monsterType.append(monster[1])
        monsterAtk.append(int(monster[2]))
        monsterDef.append(int(monster[3]))
        monsterHp.append(int(monster[4]))
    return data

def showDict(file:dict, columnLen:list[int]=None):
    if columnLen is None:
        columnLen = [(len(category) + 2) for category in file]
    for column in enumerate(file):
        nilai = str(column[1])
        makeRow(nilai, columnLen, id=column[0])
    print()
    for i in file["ID"]:
        for category in enumerate(file):
            nilai = str(file[category[1]][i-1])
            makeRow(nilai, columnLen, id=category[0])
        print()

def makeRow(nilai:str, columnLen:int, id:int):
    space = (columnLen[id]-len(nilai))
    print(nilai, space * " " + "|", end=" ")

def buatMonster(data:dict):
    namaMonster = data["Type"]
    while True:
        display("Memulai pembuatan Monster...")
        time.sleep(2)
        nama = input("Masukkan Type / Nama : ")
        if nama in namaMonster:
            print("Nama sudah terdaftar, coba lagi!")
        else:
            ATK = isDigit(input("Masukkan ATK Power : "))
            DEF = inputDEF()
            HP = isDigit(input("Masukkan HP : "))
            print("Sedang membuat monster...")
            time.sleep(3)
            clear()
            display(
f"""Monster baru berhasil dibuat!
Type      : {nama}
ATK Power : {ATK}
DEF Power : {DEF}
HP        : {HP}""")
            isTambah = YesOrNo(input("Tambahkan Monster ke database (Y/N):"))
            if isTambah:
                return [True, [nama, ATK, DEF, HP]]
            else:
                isExit = YesOrNo(input("<///> Keluar (Y/N): "))
                clear()
                if isExit:
                    return[False]

def inputDEF():
    while True:
        DEF = isDigit(input("Masukkan DEF Power (0-50) :"))
        if 0 <= DEF <= 50:
            return DEF
        else:
            print("DEF Power harus bernilai 0-50, coba lagi!")

monsterManangement()

