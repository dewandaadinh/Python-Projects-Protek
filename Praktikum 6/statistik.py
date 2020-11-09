def sum(*Angka1):
    total = 0
    for angka2 in Angka1:
        total += angka2
    return total

def average(*Angka1):
    count = 0
    for angka2 in Angka1:
        count += 1
    return sum(*Angka1) / count

def maks(*Angka1):
    max = Angka1[0]
    for angka2 in Angka1:
        if(angka2 > max):
            max = angka2
    return max

def min(*Angka1):
    min = Angka1[0]
    for angka2 in Angka1:
        if(angka2 < min):
            min = angka2
    return min
