myfile = open('G:\Kuliah semester 1\Protek\Python Projects\Python-Projects-Protek\praktikum 10/number1.txt','r')
ganjil = 0
genap = 0
i = 0
number = myfile.readlines()

for lists in number:
    if int(number[i]) % 2 == 0 :
        genap += 1
        
    else:
        ganjil += 1
        
    
    i += 1
print('banyaknya angka ganjil adalah :', ganjil)
print('banyaknya angka genap adalah  :', genap)


