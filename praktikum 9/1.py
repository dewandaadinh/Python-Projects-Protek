def ubahHuruf (teks, a, b):
    #Mengubah teks menjadi list
    daftarHuruf = list (teks)
    baru = []
    for i in range (len(daftarHuruf)):
        huruf = listHuruf[i]
        #mengganti huruf
        if huruf == a:
            huruf = b
        baru = baru + [huruf]
        #gabung list
        hasil = "".join(baru)
        return hasil
    y = ubahHuruf ('MATEMATIKA', 'T', 'S')
    print(y)
        
