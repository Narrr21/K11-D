def usePotion(status:list, potionUser:dict, maxPilihan:int, allies:dict, maxHp:int):
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih potion: "), [str(i+1) for i in range(maxPilihan)]))
        if pilihan-1 == len(status):
            clear()
            return True
        typePotion = [potion for potion in potionUser][pilihan-1]
        quantity = int(potionUser[typePotion])
        if quantity == 0:
            print(f"{typePotion} potion sudah habis")
        elif status[typePotion] == "1":
            print("sudah digunakan")
        else:
            print(f"{typePotion} potion digunakan")
            quantity -= 1
            potionUser[typePotion] = str(quantity)
            if typePotion == "Strength":
                allies["Atk"] += int(5 / 100 * allies["Atk"])
            elif typePotion == "Resilience":
                allies["Def"] += int(5 / 100 * allies["Def"])
            elif typePotion == "Healing":
                allies["HP"] += int(25 / 100 * maxHp)
                if allies["HP"] > maxHp:
                    allies["HP"] = maxHp
            status[typePotion] = str(1)
            sleep(2)
            return False