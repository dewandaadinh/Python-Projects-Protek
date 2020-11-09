def faktorial(n):
    hasil = n
    while(n > 1):
        n -= 1
        hasil *= n
    return hasil

def C(n,m):
    return faktorial(n)/(faktorial(n - m) * faktorial(m))

def P(n,m):  
    return faktorial(n) / (faktorial(n-m))  

print(P(5,3))
print(C(10,7))
