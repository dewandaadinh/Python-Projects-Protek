def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    return [a, b, c]

print(dataStat([7, 8, 2]))
