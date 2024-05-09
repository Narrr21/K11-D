from share import display, sleep, clear, writecsv, YesOrNo
from load import load, showDict

def register(dataUser:dict):
    while True:
        id = len(dataUser["ID"]) + 1
        namaUser = inputName(dataUser)
        password = inputPass()
        newUser = {
            "ID" : id,
            "Username" : namaUser,
            "Password" : password,
            "Role" : "agent",
            "OC" : 0
        }
        showDict(newUser)
        isRegister = YesOrNo(input("Registrasi Akun ? (Y/N): "))
        if not isRegister:
            clear()
            continue
        content = f"{id};{namaUser};{password};agent;0"
        writecsv(content, "user")
        print("registering your account...")
        sleep(3)
        clear()
        display("account registered")
        break

def inputName(data:dict) -> str:
    while True:
        namaUser = input("Masukkan userName: ")
        if namaUser in data["Username"]:
            print("Username sudah ada, masukkan nama lain! ")
        else:
            return namaUser

def inputPass() -> str:
    while True:
        password = input("Masukkan Password: ")
        confirm = input("Masukkan lagi (confirm): ")
        if password == confirm:
            return password
        else:
            print("password berbeda, masukkan password lagi!")

dataUser = load("user")
login = False
if not login:
    register(dataUser)