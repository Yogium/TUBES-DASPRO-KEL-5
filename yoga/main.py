import database
import commands
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", nargs = '?', default = "")
args = parser.parse_args()
if args.nama_folder == "csv_folder": #asumsi semua file eksternal tersimpan dalam folder yang bernama csv_folder
    print("Loading...")
    users = database.load("user.csv", database.users)
    candi = database.load("candi.csv", database.candi)
    bahan_bangunan = database.load("bahan_bangunan.csv", database.bahan_bangunan)
    while True:
        masukan = input(">>> ")
        commands.run(masukan)
elif args.nama_folder == '':
    print("Tidak ada nama folder yang diberikan!")
else:
    print(f"Folder {args.nama_folder} tidak ditemukan")
