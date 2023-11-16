a = (64**30) + (2**300) -32
af = ''
while a>0:
    af = str(a%4)+af
    a = a//4
    
print(str(af).count('3'))
