a= int(input("masukkan nilai b. indo:"))
b= int(input("masukkan nilai ipa:"))
c= int(input("masukkan nilai mtk:"))

if (0<=a<=100) and (0<=b<=100) and (0<=c<=100):
    if (60<=a<=100) and (60<=b<=100) and (70<=c<=100):
        print("lulus")
    elif (0<=a<60)and (0<=b<60)and (0<=c<70):
        print("tidak lulus")
else:
    print("maaf input ada yang tidak valid")


