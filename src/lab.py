import os
from share import YesOrNo, display, monsterList, level, get_stats, search, readcsv, pilihanValid, clear

def laboratory():
    # SPESIFIKASI
    # Menjalankan laboratory agar pemain dapat mengupgrade monsternya
    # selesai saat monster sudah diupgrade atau user memilih untuk keluar
    # KAMUS
    # exit = YesOrNo
    # monsterId = int
    # ALGORITMA
    clear()
    while True:
        userId = 3 #Placeholder
        labMenu(userId)
        data:list = pilihMonsterLab(userId)
        monsterId = data[0]
        levelMonster = data[1]
        upgrade(monsterId, levelMonster)
        isExit = YesOrNo(input("<///> Keluar (Y/N): "))
        if isExit:
            break

def labMenu(userId:int):
    # SPESIFIKASI
    # Menampilkan interface lab dengan list Monster dan list harga
    # KAMUS
    # AlGORITMA
    print("Selamat datang di Lab Dokter Asep !!!")
    monsterList(userId)
    print(
"""<============> UPGRADE PRICE <============>
1. Level 1 -> Level 2: 300 OC
2. Level 2 -> Level 3: 500 OC
3. Level 3 -> Level 4: 800 OC
4. Level 4 -> Level 5: 1000 OC""")

def pilihMonsterLab(userId:int) -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    data = readcsv("monster_inventory")
    hasil = search(0, str(userId), data)
    while True:
        pilihan = pilihanValid(input("<///> Pilih monster: "), [str(i+1) for i in range(len(hasil))])
        clear()
        if 0 < pilihan < len(hasil)+1:
            levelMonster = level(userId, hasil[pilihan-1][1])
        else:
            levelMonster = 0
        
        if levelMonster == 5:
            print("max level")
        elif 0 < pilihan < len(hasil)+1:
            return [hasil[pilihan-1][1], levelMonster]
        else:
            print("pilihan tidak tersedia!")

def upgrade(monsterId:int, levelMonster:int):
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
    display(
f"""{namaMonster} akan di-upgrade ke level {levelMonster + 1}
Harga untuk melakukan upgrade {namaMonster} adalah {hargaUpgrade} OC""")
    isUpgrade = YesOrNo(input("<///> Lanjutkan upgrade (Y/N): "))
    clear()
    if isUpgrade:
        #merubah data csv monster_inventory dan oc user
        display(f'Selamat, {namaMonster} berhasil di-upgrade ke level {levelMonster + 1} !')

laboratory()


