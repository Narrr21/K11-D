from share import readcsv, search

def getPotionUser(userId:int):
    inventPotion = readcsv("item_inventory")
    potionUser = search(0, str(userId), inventPotion)
    quantity = [0 for _ in range(3)]
    for potion in potionUser:
        if potion[1] == "Healing":
            quantity[0] = int(potion[2])
        elif potion[1] == "Strength":
            quantity[1] = int(potion[2])
        else: # potion[1] == "Resilience"
            quantity[2] = int(potion[2])
    data:dict = {
        "Healing" : quantity[0],
        "Strength" : quantity[1],
        "Resilience" : quantity[2],
    }
    return data

def tambahPotion(type:str, quanntity:int, dataPotion:dict):
    dataPotion[type] += quanntity
    return dataPotion
