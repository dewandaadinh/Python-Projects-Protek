nama = input("Masukkan Nama Karyawan:")
golongan = input("Masukkan Golongan:")

if(golongan == "A"):
       gajiP = 10000000
       potongan = 0.25
elif(golongan == "B"):
        gajiP = 8500000
        potongan = 0.2
elif(golongan == "C"):
        gajiP = 7000000
        potongan = 0.15
elif(golongan == "D"):
        gajiP = 5500000
        potongan = 0.1
else:
    print("tidak valid")


Potongan = gajiP*potongan
print("Nama Karyawan :",nama)
print("gaji pokok:",gajiP)
print("potongan:",Potongan)
print("gaji bersih: ", gajiP - Potongan)
    
