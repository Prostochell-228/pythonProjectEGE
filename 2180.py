a = 5*(36**7) + (6**10) - 36
af = ''
while a>0:
    af = str(a%6)+af
    a = a//6
    
print(str(af).count('5'))
