import json
inven = "inven.json"
def lihat():
    with open("inven.json", "r", encoding = "utf-8") as f:
        data = json.load(f)
        print("DAFTAR INVENTARIS")
        for idx, item in enumerate(data, 1):
            print(f"{idx}. Nama: {item['nama']} | Harga: {item['harga']}")
def tambah():
    nama = input("Masukkan nama: ")
    harga = float(input("Masukkan harga: "))
    data_baru = {"nama": nama, "harga": harga}
    try:
        with open(inven, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append(data_baru)
    with open(inven, "w", encoding= "utf-8") as f:
        json.dump(data, f)
    print("Data berhasil ditambahkan!")
while True:
    print("MENU")
    print("1. Lihat Inventaris")
    print("2. Menambahkan")
    print("3. Keluar")
    pilih = (input("MASUKKAN PILIHAN : "))
    if pilih == "1":
        lihat()
    elif pilih == "2":
        tambah()
    elif pilih =="3":
        print("ANDA TELAJ KELUAR")
        exit()
    else:
        print("PILIHAN TIDAK VALID")