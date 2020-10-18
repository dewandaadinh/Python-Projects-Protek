tarifSewa12jam = 200000
tarifSewaLanjut1jam  = 10000
JamMulai      = 6
JamSelesai   = 23
MenitMulai    = 0
MenitSelesai = 50
lamaRental = int((JamSelesai - JamMulai) + (MenitSelesai - MenitMulai) / 60)
lamaRentahLanjut = lamaRental - 12
tarifRentalLanjut = lamaRentahLanjut * tarifSewaLanjut1jam
totalTarif = tarifSewa12jam + tarifRentalLanjut
print(totalTarif)

