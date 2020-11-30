sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print(sayur)
lagi = 'y'
while lagi == 'y':
    print('Menu : \nA. Tambah data sayur \nB. Hapus data sayur \nC. Tampilkan data sayur')
    pilihan = input('Pilihan Anda : ')

    if pilihan == 'A':
        data = input('Masukkan nama sayur yang ingin ditambahkan : ')
        sayur.append(data)
        print(data +' berhasil ditambahkan.')
        lagi = input('Ingin kembali ke menu? (y/n): ')
    elif pilihan == 'B':
        data = str(input('Ketikkan nama sayur yang ingin dihapus :'))
        try :
            sayur.remove(data)
            print('Sayur berhasil dihapus.')
        except ValueError:
            print('Nama sayur tidak ditemukan.')
        lagi = input('Ingin kembali ke menu? (y/n): ')
    elif pilihan == 'C':
        print('Data Sayur : ', sayur)
        lagi = input('Ingin kembali ke menu? (y/n): ')
