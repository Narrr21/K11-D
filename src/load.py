from share import split, search, display
def readcsv(fileName:str) -> list[list[str]]:
    with open(f'data\\{fileName}.csv', 'r') as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        value = []
        for data in enumerate(hasil[0]):
            temp = [hasil[int(j)][data[0]] for j in range(len(hasil))]
            value.append(temp)
        return value

def readcsvInvent(fileName:str, userId:int) -> list[list[str]]:
    with open (f"data\\{fileName}.csv", "r") as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        data = []
        invent = search(0, str(userId), hasil)
        for barang in invent:
            data.append([barang[1], barang[2]])
        return data

def monster() -> dict:
    data = readcsv("monster")
    monster = {
        "ID":data[0][1:],
        "Type": data[1][1:],
        "ATK_power":data[2][1:],
        "DEF_power":data[3][1:],
        "HP": data[4][1:]
    }
    return monster

def monsterShop() -> dict:
    data = readcsv("monster_shop")
    monsterShop = {
        "MonsterID":data[0][1:],
        "Stock": data[1][1:],
        "Price":data[2][1:]
    }
    return monsterShop

def user(userId:int = None) -> dict:
    data = readcsv("user")
    user = {
        "ID":data[0][1:],
        "Username": data[1][1:],
        "Password":data[2][1:],
        "Role":data[3][1:],
        "OC": data[4][1:]
    }
    if userId is not None:
        user = {
            "ID":data[0][userId],
            "Username": data[1][userId],
            "Password":data[2][userId],
            "Role":data[3][userId],
            "OC": data[4][userId]
        }
    return user

def itemShop() -> dict:
    data = readcsv("item_shop")
    itemShop = {
        "Type":data[0][1:],
        "Stock": data[1][1:],
        "Price":data[2][1:]
    }
    return itemShop

def monsterInventory(userId:int) -> dict:
    data = readcsvInvent("monster_inventory", userId)
    monsterInventory:dict = {
        "MonsterID": [barang[0] for barang in data],
        "Level": [barang[1] for barang in data]
    }
    return monsterInventory

def itemInventory(userId:int) -> dict:
    data = readcsvInvent("item_inventory", userId)
    itemInventory:dict = {
        "Type": [barang[0] for barang in data],
        "Quantity": [barang[1] for barang in data]
    }
    return itemInventory

def load(data:str=None, userId:int=None) -> dict:
    if data is None:
        return[user(), monster(), monsterShop(), itemShop()]
    else:
        if data == "monster":
            return monster()
        elif data == "monster_shop":
            return monsterShop()
        elif data == "user":
            return user(userId)
        elif data == "item_shop":
            return itemShop()

def loadInvent(userId:int, data:str=None) -> dict:
    if data is None:
        return[monsterInventory(userId), itemInventory(userId)]
    else:
        if data == "monster":
            return monsterInventory(userId)
        elif data == "potion":
            return itemInventory(userId)

def getDataUser(userId:int) -> dict:
    data = load("user")
    hasil = {
        "ID": userId,
        "Username": data["Username"][userId-1],
        "Password": data["Password"][userId-1],
        "Role": data["Role"][userId-1],
        "OC": data["OC"][userId-1]
    }
    return hasil

def showDict(data:dict):
    arr = []
    text = ""
    for i in data:
        arr.append([i, data[i]])
    for [category, value] in arr:
        space = 8 - len(category)
        row = f"{category}" + space * " " + ": " + str(value)
        text += f"""{row}
"""
    display(text[:-1])
        

if __name__ == "__main__":
    ...