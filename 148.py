for n in range(2000):
    i = bin(n)[2::]
    if i.count('1')%2==0:
        i+='0'
    else:
        i+='1'
    if i.count('1')%2==0:
        i+='0'
    else:
        i+='1'
    if int(i, 2)>130:
        print(int(i, 2))
        break