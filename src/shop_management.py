from share import monsterInventory, splitcsv, potionInventory, monsterList, potionList

def shop_management():
    monsterInventory = monsterInventory()
    potionInventory = potionInventory()
    monsterShop = monsterShop()
    itemShop = itemShop()
    monsterList = monsterList()
    potionList = potionList()
    while True:
        action = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ").lower()
        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ").lower()
            if item_type == "monster":
                show_monsters(monsterShop)
            elif item_type == "potion":
                show_potions(itemShop)
        elif action == "tambah":
            item_type = input(">>> Mau nambahin apa? (monster/potion): ").lower()
            if item_type == "monster":
                add_monster(monsterList, monsterShop)
            elif item_type == "potion":
                add_potion(potionList, itemShop)
        elif action == "ubah":
            item_type = input(">>> Mau ubah apa? (monster/potion): ").lower()
            if item_type == "monster":
                update_monster(monsterShop)
            elif item_type == "potion":
                update_potion(itemShop)
        elif action == "hapus":
            item_type = input(">>> Mau hapus apa? (monster/potion): ").lower()
            if item_type == "monster":
                delete_monster(monsterShop)
            elif item_type == "potion":
                delete_potion(itemShop)
        elif action == "keluar":
            print("Dadah Mr. Yanto, sampai jumpa lagi!")
            break
        else:
            print("Aksi tidak valid.")

def monsterShop():
    with open(r'data\monster_shop.csv', 'r') as file:
        return splitcsv(file)
    
def itemShop():
    with open(r'data\item_shop.csv', 'r') as file:
        return splitcsv(file)

def show_monsters(monsterShop):
    # Fungsi untuk menampilkan semua monster yang ada di shop 
    print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
    for monster in monsterShop:
        if int(monster[5]) > 0:
            print(f"{monster[0]}  | {monster[1]:15} | {monster[2]:10} | {monster[3]:10} | {monster[4]:4} | {monster[5]:4} | {monster[6]}")

def show_potions(itemShop):
    # Fungsi untuk menampilkan semua potion yang ada di shop
    print("ID | Type                | Stok | Harga")
    for potion in itemShop:
        if int(potion[3]) > 0:
            print(f"{potion[0]}  | {potion[1]:20} | {potion[2]:4} | {potion[3]}")

def add_monster(monsterList, monsterShop):
    # Fungsi untuk menambahkan monster ke dalam shop
    print("ID | Type          | ATK Power | DEF Power | HP   |")
    for monster in monsterList:
        if monster[1] not in [m[1] for m in monsterShop]:
            print(f"{monster[0]}  | {monster[1]:15} | {monster[2]:10} | {monster[3]:10} | {monster[4]:4} |")

    monsterId = int(input(">>> Masukkan id monster: "))
    monster = next((m for m in monsterList if m[0] == monsterId), None)
    stok = int(input(">>> Masukkan stok awal: "))
    harga = int(input(">>> Masukkan harga: "))
    
    monsterShop.append({0: monster[0], 1: monster[1], 2: monster[2], 3: monster[3], 4: monster[4], 5: stok, 6: harga })
    print(f"{monster[1]} telah berhasil ditambahkan ke dalam shop!")

def add_potion(potionList, itemShop):
    # Fungsi untuk menambahkan potion ke dalam shop
    print("ID | Type          |")
    for potion in potionList:
        if potion[1] not in [p[1] for p in itemShop]:
            print(f"{potion[0]}  | {potion[1]:20} |")

    potionId = int(input(">>> Masukkan id potion: "))
    potion = next((p for p in potionList if p[0] == potionId), None)
    stok = int(input(">>> Masukkan stok awal: "))
    harga = int(input(">>> Masukkan harga: "))
    
    itemShop.append({0: potion[0], 1: potion[1], 2: stok, 3: harga})
    print(f"{potion[1]} telah berhasil ditambahkan ke dalam shop!")

def update_monster(monsterShop):
    # Fungsi untuk mengubah nilai stok atau harga dari monster
    show_monsters()
    monsterId = int(input(">>> Masukkan id monster: "))
    monster = next((m for m in monsterShop if m[0] == monsterId), None)

    stok_baru = int(input(">>> Masukkan stok baru: "))
    if stok_baru > 0:
        monster[5] = stok_baru

    harga_baru = int(input(">>> Masukkan harga baru: "))
    if harga_baru > 0:
        monster[6] = harga_baru

    if stok_baru and harga_baru:
        print(f"{monster[1]} telah berhasil diubah dengan stok baru sejumlah {monster[5]} dan dengan harga baru {monster[6]}!")
    elif stok_baru:
        print(f"{monster[1]} telah berhasil diubah dengan stok baru sejumlah {monster[5]}!")
    elif harga_baru:
        print(f"{monster[1]} telah berhasil diubah dengan harga baru {monster[6]}!")
    else:
        print("Tidak ada perubahan yang dilakukan.")

def update_potion(itemShop):
    # Fungsi untuk mengubah nilai stok atau harga dari potion
    show_potions()
    potionId = int(input(">>> Masukkan id potion: "))
    potion = next((p for p in itemShop if p[0] == potionId), None)

    stok_baru = int(input(">>> Masukkan stok baru: "))
    if stok_baru > 0:
        potion[2] = stok_baru

    harga_baru = int(input(">>> Masukkan harga baru: "))
    if harga_baru > 0:
        potion[3] = harga_baru

    if stok_baru and harga_baru:
        print(f"{potion[1]} telah berhasil diubah dengan stok baru sejumlah {potion[2]} dan dengan harga baru {potion[3]}!")
    elif stok_baru:
        print(f"{potion[1]} telah berhasil diubah dengan stok baru sejumlah {potion[2]}!")
    elif harga_baru:
        print(f"{potion[1]} telah berhasil diubah dengan harga baru {potion[3]}!")
    else:
        print("Tidak ada perubahan yang dilakukan.")

def delete_monster(monsterShop):
    # Fungsi untuk menghapus monster dari shop
    show_monsters()
    monsterId = int(input(">>> Masukkan id monster: "))
    monster = next((m for m in monsterShop if m[0] == monsterId), None)
    if monster:
        confirm = input(f">>> Apakah anda yakin ingin menghapus {monster[1]} dari shop (y/n)? ")
        if confirm.lower() == "y":
            monsterShop.remove(monster)
            print(f"{monster[1]} telah berhasil dihapus dari shop!")
        elif confirm.lower() == "n":
            print("Operasi hapus dibatalkan")
    else:
        print("ID monster tidak ditemukan atau bukan monster. Silakan coba lagi.")

def delete_potion(itemShop):
    # Fungsi untuk menghapus potion dari shop
    show_potions()
    potionId = int(input(">>> Masukkan id potion: "))
    potion = next((p for p in itemShop if p[0] == potionId), None)
    if potion:
        confirm = input(f">>> Apakah anda yakin ingin menghapus {potion[1]} dari shop (y/n)? ")
        if confirm.lower() == "y":
            itemShop.remove(potion)
            print(f"{potion[1]} telah berhasil dihapus dari shop!")
        elif confirm.lower() == "n":
            print("Operasi hapus dibatalkan")
    else:
        print("ID potion tidak ditemukan atau bukan potion. Silakan coba lagi.")