for i in range(200):
    n = (bin(i)[2:])[::-1]
    k = n[-1]
    n = n+k
    if int(n,2)>99:
        print(i,n,int(n,2))
        break