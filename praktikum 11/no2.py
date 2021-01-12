from datetime import *
def dataPinjam():
    peminjaman = datetime.date(datetime.now())
    pengembalian = peminjaman + timedelta(days = 7)
    file = open('d:\datapinjam.txt', 'w')
    lanjut = 'y'
    while lanjut == 'y':
        kode = input('Masukkan Kode Member   : ')
        nama = input('Masukkan Nama Member   : ')
        judul = input('Masukkan Judul Buku    : ')
        listData = [kode.upper(), nama, judul, str(pinjam), str(kembali)]
        data = '|'.join(listData) + '\n'
        file.write(data)
        lanjut = input('Ulangi lagi (y/n)      : ')
        if lanjut == 'n':
            break
    
file.close()
