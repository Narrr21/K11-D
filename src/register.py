from share import split, display, sleep, clear

def register():
    with open(r"data\user.csv", "r+") as file:
        dataTemp:list = []
        for line in file:
            row = list(split(line, ";"))
            dataTemp.append(row)
        user = dataUser(dataTemp)
        id = len(user["ID"]) + 1
        namaUser = inputName(user)
        password = inputPass()
        context = f"{id};{namaUser};{password};agent;0"
        file.write(context + '\n')
        print("registering your account...")
        sleep(3)
        clear()
        display("account registered")

def dataUser(data:list) -> dict:
    userId:list = []
    username:list = []
    password:list = []
    role:list = []
    oc:list = []
    dataUser:dict = {
        "ID" : userId,
        "Username" : username,
        "Pass" : password,
        "Role" : role,
        "OC" : oc
    }
    for user in data[1:]:
        userId.append(int(user[0]))
        username.append(user[1])
        password.append(user[2])
        role.append(user[3])
        oc.append(int(user[4]))
    return dataUser

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


login = False
if not login:
    register()