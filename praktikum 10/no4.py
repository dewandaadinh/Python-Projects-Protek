myFile = open('dftrmhs.txt', 'r')
file = myFile.readlines()

pencarian = input('Masukan NIM : ' )

for i in range(len(file)):
    if(pencarian in file[i]):
        data = file[i].split('|')
        print('Data Mahasiswa')
        print('NIM : ' , data[0])
        print('Nama : ' , data[1])
        print('Alamat : ' , data[2])
        break
    else:
        print('Data Mahasiswa Tidak Ditemukan')
        break
    
