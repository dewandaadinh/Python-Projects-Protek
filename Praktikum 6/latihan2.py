#StarFor1
def starFormation1(n):
    kolom=0
    baris=n

    i=0
    while(i<=n):
        j=0
        while(j<kolom):
            print('*',end='')
            j+=1
        print('')
        i+=1
        kolom+=1

starFormation1(4)
print()
#StarFor2
def starFormation2 (n):
    kolom= n
    baris= n

    a=0
    while (a<=n):
        b=0
        while (b<kolom):
            print('*',end='')
            b+=1
        a+=1
        kolom-=1

starFormation2(4)
print()

#StarFor3
def starFormation3(n) :
    kolom = 0
    baris = n
    puncak = (n + 1) / 2
    
    a = 0
    while(a <= n):
        b = 0
        while(b < kolom) :
            print('* ' , end=' ')
            b += 1
        print()
        a += 1
        kolom += 1
        
        if(kolom == puncak) :
            
            baris = puncak
            kolom = puncak

            a = 0
            while(a <= n) :
                b = 0
                while(b < kolom) :
                    print('* ', end=' ')
                    b += 1
                print()
                a += 1
                kolom -= 1

starFormation3 (7)
print 
