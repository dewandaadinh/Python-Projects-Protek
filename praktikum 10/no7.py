enkripsi = []
hasil = []
print('=' * 50)
print("Program Penerjemah Sandi Caesar")
print('-'*50)

alamat = input ("Masukkan alamat teks yang ter-enkripsi:)
angka = int ( input("Berapa alpabhet yang ingin Anda geser?))
with open (alamat, 'r', encoding="utf-8") as sumber:
    for kata in sumber:
        for huruf in kata:
            x = ord(huruf)
            y = x - angka
            enkripsi.append(y)
print('-' * 50)
print ("Hasil telah disimpan di folder yang sama dengan kode python ini \nDengan nama \"Hasil terjemah.txt\" ")
print('=' * 50)
with open ("Hasil enkripsi.txt", 'w+', encoding="utf-8") as f:
    for data in enkripsi :
        z = chr(data)
        a = ''.join(z)
        f.write(a)



    
    

    
