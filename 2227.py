a = (7**160)*(7**90) - ((14**150) + (2**13))
af = ''
while a>0:
    af = str(a%7)+af
    a = a//7
aff = []
for i in af:
    if i!='6':
        aff.append(int(i))  
    
print(sum(aff))
