from share import YesOrNo, display, pilihanValid, clear, writecsv, displayBar
from monster import get_stats, monsterList, level
from load import getDataUser, loadInvent

def laboratory(userId:int, dataUser:dict=None):
    # SPESIFIKASI
    # Menjalankan laboratory agar pemain dapat mengupgrade monsternya
    # selesai saat monster sudah diupgrade atau user memilih untuk keluar
    # KAMUS
    # exit = YesOrNo
    # monsterId = int
    # ALGORITMA
    clear()
    dataUser = getDataUser(userId) #Placeholder
    dataMonster = loadInvent(userId, "monster") #Placeholder
    while True:
        userName = dataUser["Username"]
        OC = int(dataUser["OC"])
        jumlahPilihan = len(dataMonster["MonsterID"]) + 1
        labMenu(userId, userName, OC, dataMonster, jumlahPilihan)
        [monsterId, levelMonster] = pilihMonsterLab(dataMonster, jumlahPilihan)
        if monsterId == 0:
            break
        upgrade(monsterId, levelMonster, OC, dataUser, dataMonster)
        isExit = YesOrNo(input("<///> Keluar (Y/N): "))
        if isExit:
            break

def labMenu(userId:int, userName:str, OC:int, dataMonster:dict, jumlahPilihan:int):
    # SPESIFIKASI
    # Menampilkan interface lab dengan list Monster dan list harga
    # KAMUS
    # AlGORITMA
    print(f"Selamat datang di Lab Dokter Asep. Agent {userName} !!!")
    monsterList(userId, dataMonster)
    print(f"{jumlahPilihan}. Cancel")
    displayBar("UPGRADE PRICE")
    print(
"""1. Level 1 -> Level 2: 300 OC
2. Level 2 -> Level 3: 500 OC
3. Level 3 -> Level 4: 800 OC
4. Level 4 -> Level 5: 1000 OC""")
    print(f"Anda memiliki {OC} OC ")

def pilihMonsterLab(dataMonster:dict, jumlahPilihan:int) -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih monster: "), [str(i+1) for i in range(jumlahPilihan)]))
        if pilihan == jumlahPilihan:
            return[0, 0]
        monsterId = dataMonster["MonsterID"][pilihan-1]
        levelMonster = level(monsterId, dataMonster)
        if levelMonster == 5:
            print("max level")
        else:
            clear()
            return [monsterId, levelMonster]

def upgrade(monsterId:int, levelMonster:int, OC:int, data:dict, dataMonster:list):
    # SPESIFIKASI
    # Melakukan upgrade monster yang dipilih dengan id adalah monsterId
    # upgrade akan menambahkan 1 level pada monster dan mengurangi oc user sesuai biayanya
    # KAMUS
    # namaMonster = string
    # level, namaMonster, hargaUpgrade = int
    # isUpgrade = YesOrNo
    statMonster = get_stats(monsterId, levelMonster)
    namaMonster:str = statMonster["Name"] 
    if levelMonster == 1:
        hargaUpgrade = 300
    elif levelMonster == 2:
        hargaUpgrade = 500
    elif levelMonster == 3:
        hargaUpgrade = 800
    elif levelMonster == 4:
        hargaUpgrade = 1000
    if hargaUpgrade <= OC:
        display(
f"""{namaMonster} akan di-upgrade ke level {levelMonster + 1}
Harga untuk melakukan upgrade {namaMonster} adalah {hargaUpgrade} OC
Saat ini anda memiliki {OC} OC""")
        isUpgrade = YesOrNo(input("<///> Lanjutkan upgrade (Y/N): "))
        clear()
        if isUpgrade:
            data["OC"] = OC - hargaUpgrade
            dataMonster["Level"] = str(levelMonster + 1)
            display(f'Selamat, {namaMonster} berhasil di-upgrade ke level {levelMonster + 1} !')
    else:
        print(
f"""Anda hanya memiliki {OC} OC
butuh {hargaUpgrade} OC untuk mengupgrade {namaMonster}""")

def changeUpgrade(user:int, OC:int):
    writecsv("")

if __name__ == "__main__":
    laboratory(2)


