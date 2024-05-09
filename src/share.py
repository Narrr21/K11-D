import os
import time

def YesOrNo(masukan:str) -> str:
    masukan = str.upper(masukan)
    while True:
        if masukan != "Y" and masukan != "N":
            print("Masukan yang valid hanya Y atau N")
            masukan = str.upper(input("<///> Y/N: "))
        else:
            return masukan == "Y"

def pilihanValid(masukan:str, validRange:list[str]) -> int:
    while True:
        if masukan in validRange:
            return masukan
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

def displayBar(text:str):
    content = text + " "
    arrow = 60 - len(content)
    if arrow % 2 == 1:
        content += " "
        arrow -= 1
    arrow = int(arrow/2)
    bar = "<" + "=" * arrow + ">"
    print(bar, content, bar)

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

def arraycsv(fileName:str) -> list[list[str]]:
    with open(f'data\\{fileName}.csv', 'r') as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        return hasil

def writecsv(context:str, fileName:str):
    with open(f'data\\{fileName}.csv', 'r+') as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        file.write(context + '\n')

def index(element, array:list):
    for i in enumerate(array):
        if i[1] == element:
            return i[0]

def clear():
    os.system("cls")
    print("...")
    os.system("cls")

def sleep(waktu:int=2):
    time.sleep(waktu)

def search(searchIndex:int, searchInput:str, file:list) -> list:
    hasil = []
    for row in file:
        if searchInput == row[searchIndex]:
            hasil.append(row)
    return hasil

if __name__ == "__main__":
    ...
