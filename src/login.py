def login(users, login):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    for user_id in users:
        if users[user_id]['username'] == username:
            if users[user_id]['password'] == password:
                if username in login:
                    print("Anda telah login dengan username", username, ", silahkan lakukan 'LOGOUT' sebelum melakukan login kembali.")
                    return False
                else:
                    print("Login berhasil!")
                    login.append(username)
                    return False
            else:
                print("Password salah!")
                return False

    print("Username tidak ditemukan")
    return True