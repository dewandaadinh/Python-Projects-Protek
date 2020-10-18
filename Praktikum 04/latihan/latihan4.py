jarak_kota_A_ke_B=125
kecepatan_1=62
jarak_kota_B_ke_C=256
kecepatan_2=70
jamberangkat=6
istirahat=0.45


waktu1=jarak_kota_A_ke_B//kecepatan_1 
waktu2=jarak_kota_B_ke_C//kecepatan_2 

waktutotal=(waktu1+waktu2+istirahat)

jamsampai=jamberangkat+waktutotal

print("Pak Amir akan tiba ditujuan pada pukul ",jamsampai)
