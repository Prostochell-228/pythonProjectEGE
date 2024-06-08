s=0
for n in range(200000):
    i = bin(n)[2::]
    if i.count('1') % 2 == 0:
        i += '00'
    else:
        i += '10'
    if int(i, 2) in range(20, 51):
        s+=1
print(s)
