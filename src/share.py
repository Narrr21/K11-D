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

def pilihMonster() -> int:
    # SPESIFIKASI
    # Melakukan loop hingga valid untuk menghasilkan pilihan monster yang ingin diupgrade
    # KAMUS
    # pilihan, level = int
    # ALGORITMA
    while True:
        pilihan = int(input("<///> Pilih monster: "))
        os.system('cls')
        if 0 < pilihan < 5:#5 adalah placeholder untuk panjang list monster
            return pilihan
        else:
            print("pilihan tidak tersedia!")