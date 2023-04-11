import commands
import database
import random

candi = database.candi
bahan_bangunan = database.bahan_bangunan

def bangun():
    global candi, bahan_bangunan
    Ncandi = commands.length_eff(candi)
    if commands.role == "Pembangun":
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air = random.randint(1,5)
        if Ncandi <100:
            if bahan_bangunan[1][2] >= pasir and  bahan_bangunan[2][2] >= batu and  bahan_bangunan[3][2] >= air:
                print("Candi berhasil dibangun.")
                candi[Ncandi][0] = Ncandi
                candi[Ncandi][1] = commands.id
                candi[Ncandi][2] = pasir
                candi[Ncandi][3] = batu
                candi[Ncandi][4] = air


            else:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun")
        else: 
            if bahan_bangunan[1][2] >= pasir and  bahan_bangunan[2][2] >= batu and  bahan_bangunan[3][2] >= air:
                print("Candi berhasil dibangun.")
            else:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun")
    else:
        pass


def pengumpul():
    global bahan_bangunan
    if commands.role == "Pengumpul":
        pasir = random.randint(0,5)
        batu = random.randint(0,5)
        air = random.randint(0,5)
        bahan_bangunan[1][2] += pasir
        bahan_bangunan[2][2] += batu
        bahan_bangunan[3][2] += air
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air")
    else:
        pass