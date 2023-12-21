
for i in range(200):
    N = bin(i)[2:]
    if N.count('1')%2==0:
        N+='0'
    else:
        N+='1'
    if N.count('1') % 2 == 0:
        N += '0'
    else:
        N += '1'
    if int(N,2)>118:
            print(N,i,int(N,2))
            break