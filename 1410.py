a = (4**625) - (2**311) +(2**571) - 48
af = ''
while a>0:
    af = str(a%4)+af
    a = a//4
    
print(str(af).count('1'))
