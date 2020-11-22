masukan = input("Masukkan nama file : ")

try:
    file = open(masukan,'r')
    lagi = 'y'
    while lagi == 'y': 
        file = open(masukan,'a')
        append = input("Data yang mau ditambahkan :")
        file.write(append)
        lagi = input("Mau lagi (y/n)?")
        file.close()
except FileNotFoundError:
    print('file tidak ditemukam/salah ketik')
