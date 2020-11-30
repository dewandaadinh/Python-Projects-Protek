buah={'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
for x in buah.items():
    data=list(buah.values())
    data.sort(reverse=True)
    max(data)
print(data)
