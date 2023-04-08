def load(name_file : str, mat)->list[list[str]]:
    mat = csv_parser(name_file)
    return mat

def csv_parser(name_file):
    if name_file == "user.csv":
        mat = [["" for j in range(3)] for i in range(103)]
    elif name_file == "candi.csv":
        mat = [["" for j in range(5)] for i in range(101)]
    elif name_file == "bahan_bangunan.csv":
        mat = [["" for j in range(3)] for i in range(4)]
    file = open(name_file)
    reader = file
    countCol = 1
    for line in reader:
        for i in range(len(line)):
            if line[i] == "\n" or line[i] == ';':
                countCol +=1
                if line[i] == "\n":
                    countCol = 1

    file = open(name_file) #file akan auto close jika sudah melakukan iterasi for line in reader
    reader = file
    i = 0; j = 0
    for line in reader:
        s = ''
        for idx in range(len(line)):
            if line[idx] != "\n" and line[idx] != ';':
                s+=line[idx]
            else:
                mat[i][j] = s
                s = ''
                j += 1
        if j == countCol-1 :
            mat[i][j] = s
        else:
            j = 0
        i +=1
    return mat

users = []
bahan_bangunan = []
candi = []
users = load("user.csv", users)
bahan_bangunan = load("bahan_bangunan.csv",bahan_bangunan)
candi = load("candi.csv",candi)