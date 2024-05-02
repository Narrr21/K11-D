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