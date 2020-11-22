namafile = input("Masukkan nama file : ")

try:
    file = open(namafile,'r')
    print('isi file',namafile,'adalah : ',file.read())
except FileNotFoundError:
    print('file tidak ada/ salah penulisan')
