a = (16**820) - (2**761) + 14
af = ''
while a>0:
    af = str(a%4)+af
    a = a//4
    
print(str(af).count('0'))
