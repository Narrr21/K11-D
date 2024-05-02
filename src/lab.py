import os

class YesOrNo:
    def __init__(self, YN):
        while True:
            if YN != "Y" and YN != "N":
                print("Masukan yang valid hanya Y atau N")
                YN = input("<///> Y/N: ")
                os.system('cls')
            else:
                break
        self.YN = YN

def display(text:str):
    print(f"""
<==================================================================================>
{text}
<==================================================================================>""")

def laboratory():
    # SPESIFIKASI
    # Menjalankan laboratory agar pemain dapat mengupgrade monsternya
    # selesai saat monster sudah diupgrade atau user memilih untuk keluar
    # KAMUS
    # selesai = boolean
    # exit = YesOrNo
    # monsterId = int
    # ALGORITMA
    selesai:bool = False
    while not selesai:
        labMenu()
        exit = YesOrNo(input("<///> Keluar (Y/N): "))
        if exit.YN == "Y":
            break
        monsterId:int = pilihMonster()
        selesai = upgrade(monsterId)

def labMenu():
    # SPESIFIKASI
    # Menampilkan interface lab dengan list Monster dan list harga
    # KAMUS
    # AlGORITMA
    print("""
Selamat datang di Lab Dokter Asep !!!
                  
<============> MONSTER LIST <============>""")
    print("monster")#placeholder tampilan list monster
    print("""
<============> UPGRADE PRICE <============>""")
    print("harga")#placeholder tampilan list harga

def pilihMonster() -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    while True:
        pilihan = int(input("<///> Pilih monster: "))
        os.system('cls')
        if pilihan in range(1, 5):#5 adalah placeholder untuk panjang list monster
            level:int = 2 #placeholder untuk level monster
            if level == 5:
                print("Maaf monster yang Anda pilih sudah memiliki level maksimum")
            else:
                return pilihan
        else:
            print("pilihan tidak tersedia!")

def upgrade(monsterId:int) -> bool:
    # SPESIFIKASI
    # Melakukan upgrade monster yang dipilih dengan id adalah monsterId
    # upgrade akan menambahkan 1 level pada monster dan mengurangi oc user sesuai biayanya
    # KAMUS
    # namaMonster = string
    # level, namaMonster, hargaUpgrade = int
    # isUpgrade = YesOrNo
    namaMonster:str = "Chacha" #placeholder nama monster
    level:int = 2 #placeholder untuk level monster
    hargaUpgrade:int = 300 #placeholder untuk biaya upgrade
    display(
f"""{namaMonster} akan di-upgrade ke level {level + 1}
Harga untuk melakukan upgrade {namaMonster} adalah {hargaUpgrade} OC""")
    isUpgrade = YesOrNo(input("<///> Lanjutkan upgrade (Y/N): "))
    os.system("cls")
    if isUpgrade.YN == "Y":
        #merubah data csv monster_inventory dan oc user
        display(f'Selamat, {namaMonster} berhasil di-upgrade ke level {level + 1} !')
        return True
    elif isUpgrade.YN == "N" :
        return False

laboratory()


