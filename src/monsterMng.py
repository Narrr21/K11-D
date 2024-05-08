from share import pilihanValid, YesOrNo, clear, display, isDigit, sleep
from load import load

def monsterManangement():
    dataMonster = load("monster")
    while True:
        clear()
        print(dataMonster)
        print(
"""<================================================================>
SELAMAT DATANG DI DATABASE PARA MONSTER !!!
1. Tampilkan semua Monster
2. Tambah Monster Baru""")
        pilihan = int(pilihanValid(input("<///> Pilih perintah: "), ["1", "2"]))
        
        if pilihan == 1:
            showMonsterData(dataMonster, columnLen=[2, 12, 10, 10, 6])
        else : # pilihan == 2
            [isMade, [monsterID, namaMonster, ATK, DEF, HP]] = buatMonster(dataMonster)
            if isMade:
                dataMonster["ID"].append(str(monsterID))
                dataMonster["Type"].append(str(namaMonster))
                dataMonster["ATK_power"].append(str(ATK))
                dataMonster["DEF_power"].append(str(DEF))
                dataMonster["HP"].append(str(HP))
            else:
                break
        isKeluar = YesOrNo(input("<///> Keluar (Y/N): "))
        if isKeluar:
            break

def showMonsterData(file:dict, columnLen:list[int]=None):
    if columnLen is None:
        columnLen = [(len(category) + 2) for category in file]
    for column in enumerate(file):
        nilai = str(column[1])
        makeRow(nilai, columnLen, id=column[0])
    print()
    for i in file["ID"]:
        for category in enumerate(file):
            nilai = str(file[category[1]][int(i)-1])
            makeRow(nilai, columnLen, id=category[0])
        print()

def makeRow(nilai:str, columnLen:int, id:int):
    space = (columnLen[id]-len(nilai))
    print(nilai, space * " " + "|", end=" ")

def buatMonster(data:dict):
    namaMonster = data["Type"]
    display("Memulai pembuatan Monster...")
    sleep(2)
    while True:
        nama = input("Masukkan Type / Nama : ")
        if nama in namaMonster:
            print("Nama sudah terdaftar, coba lagi!")
        else:
            monsterID = len(namaMonster) + 1
            ATK = isDigit(input("Masukkan ATK Power : "))
            DEF = inputDEF()
            HP = isDigit(input("Masukkan HP : "))
            print("Sedang membuat monster...")
            sleep(3)
            clear()
            display(
f"""Monster baru berhasil dibuat!
Type      : {nama}
ATK Power : {ATK}
DEF Power : {DEF}
HP        : {HP}""")
            isTambah = YesOrNo(input("Tambahkan Monster ke database (Y/N):"))
            if isTambah:
                return [True, [monsterID, nama, ATK, DEF, HP]]
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

