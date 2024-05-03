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

def split(baris:str, pemisah:str=None):
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

def splitcsv(file:list):
    hasil:list = []
    for line in file:
        row = list(split(line, ";"))
        hasil.append(row)
    return hasil

def monsterInventory() -> list:
    with open(r'data\monster_inventory.csv', 'r') as file:
        return splitcsv(file)

def monsterList(userId:int) -> list:
    data = monsterInventory()
    hasil = search(0, str(userId), data)
    return hasil

def search(searchIndex:int, searchInput, file:list) -> list:
    hasil = []
    for row in file:
        if searchInput == row[searchIndex]:
            hasil.append(row)
    return hasil
