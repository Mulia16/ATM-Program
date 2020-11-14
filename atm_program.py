import random
from datetime import datetime
from customer import Customer

customers = {}

while True:
    print("1. Membuat akun")
    print("2. Masuk akun")
    print("3. keluar")
    
    chooseAction = int(input("Masukkan angka untuk memilih menu: "))
    if chooseAction == 1:
        newId = int(input("Masukkan ID: "))
        newPin = int(input("Masukkan Pin: "))
        customers[newId] = Customer(newId, custPin=newPin)
        print("Berhasil membuat akun\n")

    elif chooseAction == 2:
        while True:
            id = int(input("Masukkan ID anda: "))
            if not id in customers :
                print("Error. ID anda tidak terdaftar")
                continue
            break
        
        trial = 0
        customer = customers[id]
        while True:
            pin = int(input("Masukkan pin anda: "))
            if customer.getCustPin() != pin : 
                print("Error. Pin anda salah")
                trial += 1
                if trial == 3:
                    print("Error. Tolong pastikan pin anda dengan benar dan silahkan coba lagi")
                    exit()
                continue
            break

        while True:
            print("\nSelamat Datang")
            print("Menu Utama:")
            print("1. Cek Saldo")
            print("2. Debet")
            print("3. Simpan")
            print("4. Ganti Pin")
            print("5. Keluar")

            chooseMenu = int(input("Masukkan angka untuk memilih menu: "))
            if chooseMenu == 1:
                print("Saldo Anda : " + str(customer.getCustBalance()))
            elif chooseMenu == 2:
                nominal = int(input("Masukkan nominal Debet: "))
                customer.withdrawBalance(nominal)
                print("Saldo Anda : " + str(customer.getCustBalance()))
            elif chooseMenu == 3:
                nominal = int(input("Masukkan nominal Simpan: "))
                customer.depositBalance(nominal)
                print("Saldo Anda : " + str(customer.getCustBalance()))
            elif chooseMenu == 4:
                pin = int(input("Masukkan pin baru: "))
                verify = int(input("Masukkan pin verifikasi(lama): "))
                customer.setCustPin(pin, verify)
            elif chooseMenu == 5:
                print("Nomor Record : " + str(random.randint(100_000, 1_000_000)))
                print("Tanggal : " + datetime.now().date().strftime("%d-%m-%Y"))
                print("Sisa Saldo : " + str(customer.getCustBalance()))
                exit()
