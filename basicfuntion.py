def le(a):
    #dipakai untuk menghitung banyak element dalam suatu array
    #kamus lokal:
    #count: Int
    #a : array
    count = 0
    for i in a:
        count +=1
    return count

def app(a, b):
    x = [0 for i in range(1)]
    x[0] = b
    a = a + x
    return a

def po(a, n):
    b = [0 for i in range(le(a)-1)]
    rem = False
    for i in range(le(a)):
        if i == n:
            rem = True
        elif rem==False and i!=n:
            b[i]= a[i]
        else:
            b[i-1]=a[i]
    return b