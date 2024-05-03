import os

def YesOrNo(YN:str) -> str:
    while True:
        if YN != "Y" and YN != "N":
            print("Masukan yang valid hanya Y atau N")
            YN = input("<///> Y/N: ")
            os.system('cls')
        else:
            break
    return YN

def display(text:str):
    print(f"""
<==================================================================================>
{text}
<==================================================================================>""")