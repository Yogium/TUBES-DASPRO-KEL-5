import database
def length_eff(l):
    i = 0
    count = 0
    while l[i][0] != '':
        count +=1 
        i += 1
    return count

users = database.users
Neff = length_eff(users)
Login = False
def login() :
    global Login, Neff, username, password, role
    if Login == True:
        print("Login gagal!")
        print(f'Anda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali')
        return Login
    while not(Login) :
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
        for i in range (1,Neff) :
            if (username == users[i][0]) and (password == users[i][1]) :
                Login = True
                role = users[i][2]
                print ("Selamat datang", users[i][0],"!")
                print ("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                
        
        if not(Login):
            wrongpw = False
            for i in range(1,Neff):
                if (username == users[i][0]) and (password != users[i][1]) :
                    print ("Password Salah !")
                    wrongpw = True
            if not(wrongpw):
                print("Username tidak terdaftar")    

def logout():
    global Login
    if Login == False:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        Login = False

def summonjin():
    global users, Neff
    if Neff < 103:
        tipeJin = ["Pengumpul","Pembangun"]
        print("Jenis jin yang dapat dipanggil")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        noJin = int(input("Masukkan nomor jenis jin yang akan dipanggil: "))
        if noJin == 1 or noJin == 2:
            roleJin = tipeJin[noJin-1]
            print(f"Memilih jin {roleJin}")

        else:
            while noJin != 1 and noJin != 2:
                print(f"Tidak ada jenis jin bernomor {noJin}")
                noJin = int(input("Masukkan nomor jenis jin yang akan dipanggil: "))
            if noJin == 1 or noJin == 2:
                roleJin = tipeJin[noJin-1]
                print(f"Memilih jin {roleJin}")
        usernameJin =  input("Masukkan username jin: ")
        while True:
            diambil = False
            for i in range(3,100):
                if usernameJin == users[i][0]:
                    print(f"{usernameJin} sudah diambil")
                    diambil = True
                    usernameJin = input("Masukkan username jin: ")
            if diambil == False:
                break
        passwordJin = input("Masukkan password jin: ")
        while True:
            if len(passwordJin) > 25 or len(passwordJin) < 5:
                print("Password panjangnya harus 5-25 karakter!")
            else:
                break
            passwordJin = input("Masukkan password jin: ")
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"Jin {usernameJin} berhasil dipanggil")
        users[Neff][0] = usernameJin
        users[Neff][1] = passwordJin
        users[Neff][2] = roleJin
        Neff += 1
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    
def hapusjin():
    pass

def ubahjin():
    global users,Neff
    usernameJin = input("Masukkan username jin: ")
    ditemukan = False
    for i in range(Neff):
        if usernameJin == users[i][0] :
            if users[i][2] == "Pengumpul":
                ditemukan = True
                konfirmasi = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
                if konfirmasi == 'Y':
                    users[i][2] = "Pembangun"
            else :# users[i][2] == "Pembangun"
                ditemukan = True
                konfirmasi = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul" (Y/N)? ')
                if konfirmasi == 'Y':
                    users[i][2] = "Pengumpul"
    if not(ditemukan):
        print("Tidak ada jin dengan username tersebut")

def run(module):
    if module == "login":
        login()
    elif module == "logout":
        logout()
    if Login:
        if role == "bandung_bondowoso":
            if module == "summonjin":
                summonjin()
            elif module == "hapusjin":
                hapusjin()
            elif module == "ubahjin":
                ubahjin()
        elif role == "roro_jonggrang":
            pass
        elif role == "pengumpul":
            pass
        elif role == "pembangun":
            pass