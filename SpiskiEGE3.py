a = []
for i in range(11000011, 10**8):
    j = str(i)
    if len(j)==8 and j[0]=="1" and j[1]=="1" and j[-1]=="1" and j[-2]=="1":
        if int(j[2])%2==0 and int(j[-3])%2!=0 and i%2023==0:
            a.append([i, i//2023])
print(sorted(a))
