namaFile = open('G:\Kuliah semester 1\Protek\Python Projects\Python-Projects-Protek\praktikum 10/angka.txt', 'r')
file = namaFile.readlines()

for i in range(len(file)):
    angka1 = file[i].replace('\n','')
    angka2 = angka1.split('|')
    jumlah = int(angka2[0]) + int(angka2[1])
    file[i] = jumlah
    
print('Hasil jumlah di hasilAngka.txt')

namaFile.close()
hasil = open('G:\Kuliah semester 1\Protek\Python Projects\Python-Projects-Protek\praktikum 10/hasilAngka.txt', 'w')
for x in range(len(file)):
    hasil.write(str(file[x]) + '\n')
hasil.close()
