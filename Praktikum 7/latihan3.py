print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

lagi = 'y'
datamasuk = 0
totalnya = 0
while lagi == 'y':
    try:
        bil = int(input("Masukkan bilangan bulat : "))
        totalnya += bil
        datamasuk += 1
        lagi = input("Lagi (y/n)?")
    except ValueError:
        print("Bukan bilangan bulat")

if(datamasuk != 0):
    print('\nRata-ratanya adalah', totalnya/datamasuk)
else:
    print('\ndatanya tidak valid')
