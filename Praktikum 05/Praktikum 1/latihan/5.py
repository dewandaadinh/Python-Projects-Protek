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
#Tunjangan
StatKaryawan= input("Masukkan Status (1:menikah, 2:Belum): ")
if(StatKaryawan == "1"):
  status = "Sudah Menikah"
  tunNikah = 0.1
  anak = input("Masukkan jumlah anak : ")
  tunAnak = int(anak) * 0.05
elif(StatKaryawan == "2"):
  status = "Belum Menikah"
  tunNikah = 0
  anak = "0"
  tunAnak = 0


GajiKotor = gajiP+(gajiP*tunAnak)+(gajiP*tunNikah)
GajiBersih = GajiKotor-(gajiP*potongan)
print("Nama Karyawan :",nama)
print("Golongan:",golongan)
print("Status Menikah:",status)
print("Jumlah anak:",anak)
print("-------------------------")
print("gaji pokok:",gajiP)
print ("Tunjangan Nikah  :"+str(int(gajiP*tunNikah)))
print ("Tunjangan Anak   :"+str(int(gajiP*tunAnak)))
print ("__________________________________________+")
print ("Gaji Kotor       :Rp"+str(int(GajiKotor)))
print ("potongan("+str(potongan*100)+ "%)  : rp" +str(int(gajiP*potongan)))
print ("__________________________________________-")
print ("GajiBersih    :Rp"+str(int(GajiBersih)))
    
