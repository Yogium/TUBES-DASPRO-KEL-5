def slice(arr: list, start: int, stop:int)-> list:
    # Mendapatkan array yang dislice elemennya dari element start hingga stop-1
    temp = []
    for i in range(start,stop):
        temp += [arr[i]]
    return temp

def length(arr: list)-> int:
    # Menentukan panjang array, serupa dengan len() pada python
    count = 0
    for item in arr:
        count += 1
    return count

def add(item, arr: list)-> list:
    # Menambahkan item ke elemen terakhir array, serupa dengan append() pada python 
    temp = [0 for i in range(length(arr)+1)]
    for i in range(length(temp)):
        if i < length(arr):
            temp[i] = arr[i]
        else:
            temp[i] = item
    arr = temp
    return arr

def rmv(item,arr: list)-> list:
    # Menghapus item dari elemen array, serupa dengan remove() pada python
    temp = []
    for i in range(length(arr)):
        if arr[i] != item :
            temp = add(arr[i],temp)
    return temp

def csv_parser(name_file):
    # Mengkonversikan data pada csv ke matriks
    file = open(name_file)
    reader = file.read()
    mat = []
    row = []
    s = ""
    for char in reader:
        if char != ',' and char != '\n':
            s += char
        else:
            row = add(s,row)
            s = ""
            if char == '\n' :
                mat = add(row,mat)
                row = []
    row = add(s,row)
    mat = add(row,mat)
    return mat
