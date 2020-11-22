file = open("G:\Kuliah semester 1\Protek\Python Projects\Python-Projects-Protek\Praktikum 7/data1.txt", "r")
sum = 0
for data in file:
    try:
        sum = sum + int(data)
        print(sum)
    except ValueError:
        print('ini string')
