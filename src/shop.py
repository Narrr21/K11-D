from share import monsterInventory, splitcsv, potionInventory

def shop(owca_coin):
    monsterInventory = monsterInventory()
    potionInventory = potionInventory()
    monsterShop = monsterShop()
    itemShop = itemShop()
    while True:
        action = input(">>> Pilih aksi (lihat/beli/keluar): ").lower()
        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ").lower()
            if item_type == "monster":
                show_monsters(monsterShop)
            elif item_type == "potion":
                show_potions(itemShop)
        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {owca_coin}.")
            item_type = input(">>> Mau beli apa? (monster/potion): ").lower()
            if item_type == "monster":
                monster_id = int(input(">>> Masukkan id monster: "))
                owca_coin = buy_monster(monster_id, owca_coin, monsterShop)
            elif item_type == "potion":
                potion_id = int(input(">>> Masukkan id potion: "))
                quantity = int(input(">>> Masukkan jumlah: "))
                owca_coin = buy_potion(potion_id, quantity, owca_coin, itemShop)
        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
        else:
            print("Aksi tidak valid.")
    return owca_coin

def monsterShop():
    with open(r'data\monster_shop.csv', 'r') as file:
        return splitcsv(file)
    
def itemShop():
    with open(r'data\item_shop.csv', 'r') as file:
        return splitcsv(file)

def show_monsters(monsterShop):
    print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
    for monster in monsterShop:
        if int(monster[5]) > 0:
            print(f"{monster[0]}  | {monster[1]:15} | {monster[2]:10} | {monster[3]:10} | {monster[4]:4} | {monster[5]:4} | {monster[6]}")

def show_potions(itemShop):
    print("ID | Type                | Stok | Harga")
    for potion in itemShop:
        if int(potion[3]) > 0:
            print(f"{potion[0]}  | {potion[1]:20} | {potion[2]:4} | {potion[3]}")

def buy_monster(id, owca_coin, monsterShop):
    monster = next((m for m in monsterShop if m[0] == id), None)
    if monster:
        if int(monster[5]) > 0 and int(monster[6]) <= owca_coin and id not in monsterInventory:
            monster[5] = str(int(monster[5]) - 1)
            print(f"Berhasil membeli item: {monster[1]}. Item sudah masuk ke inventory-mu!")
            monsterInventory.append([id, monster[1], 1])
            return owca_coin - int(monster[6])
        elif id in [m[0] for m in monsterInventory]:
            print(f"Monster {monster[1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
        elif int(monster[5]) == 0:
            print("Stok monster ini habis!")
        else:
            print("OC-mu tidak cukup.")
    else:
        print("Monster tidak ditemukan.")
    return owca_coin

def buy_potion(id, quantity, owca_coin, itemShop):
    potion = next((p for p in itemShop if p[0] == id), None)
    if potion:
        total_price = int(potion[3]) * quantity
        if int(potion[2]) >= quantity and total_price <= owca_coin:
            potion[2] = str(int(potion[2]) - quantity)
            potionInventory.append([id, potion[1], quantity])
            print(f"Berhasil membeli item: {quantity} {potion[1]}. Item sudah masuk ke inventory-mu!")
            return owca_coin - total_price
        elif int(potion[2]) < quantity:
            print("Stok potion tidak cukup!")
        else:
            print("OC-mu tidak cukup.")
    else:
        print('Potion tidak ditemukan.')
    return owca_coin