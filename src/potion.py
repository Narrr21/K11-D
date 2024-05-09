from load import loadInvent
from share import displayBar

def getPotion(userId:int):
    potionUser = loadInvent(userId, "potion")
    data = {}
    for [i ,potion] in enumerate(potionUser["Type"]):
        quantityPotion = int(potionUser["Quantity"][i])
        if quantityPotion > 0:
            data[potion] = str(quantityPotion)
    return data

def potionStatus(potionUser):
    status = {}
    for potion in potionUser:
        status[potion] = str(0)
    return status

def tambahPotion(type:str, quanntity:int, dataPotion:dict):
    dataPotion[type] += quanntity
    return dataPotion

def potionList(potionUser:dict) -> int:
    displayBar("POTION LIST")
    for [i, potion] in enumerate(potionUser):
        space = 12 - len(potion)
        print(f"{i+1}. {potion} Potion" + space * " " + f"(Qty: {potionUser[potion]})", end="")
        if potion == "Strength":
            print(" - Increase ATK Power")
        elif potion == "Resilience":
            print(" - Increase DEF Power")
        elif potion == "Healing":
            print(" - Restore Health")
        else: 
            print()
    max = len(potionUser) + 1
    print(f"{max}. Cancel")
    return max

if __name__ == "__main__":
    potionUser = getPotion(3)
    # print(potionUser)
    # potionList(potionUser)
    # print(potionStatus(potionUser))