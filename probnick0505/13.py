s = 0
for i in range(512):
    n = bin(i)[2::]

    if n.count('1')>=7:
        print(n)
        s+=1
print(s)