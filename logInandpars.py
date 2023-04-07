def csv_pars (csv) :
    # Untuk mengubah data csv menjadi sebuah matriks data
    file = [[0 for i in range(banyak_kolom)] for i in range (banyak_baris)]
    data = 0
    while data < panjang_baris :
        item = ""
        counter_baris = 0
        for j in csv :
            if j == "\n" :
                file[data][counter] = item
                counter_baris = 0
                data += 1
                item = ""
            elif j == ";" :
                file[data][counter] = item
                counter_baris += 1
                item = ""
    return(file)


def login () :
    notLogin = True
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    while notLogin :
        for i in range (1,panjang_matriks(username)) :
            if (username == user[i][1]) and (password == user[i][2]) :
                notLogin = False
                print ("Selamat datang", user[i][1],"!")
                print ("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
            elif (username == user[i][1]) and (password != user[i][2]) :
                print("Username tidak terdaftar")
            elif (username != user[i][1] ) and (password == user[i][2]) :
                print ("Password Salah !")
