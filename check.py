for i in range(200):
    N = bin(i)[2:]
    if sum(map(int,N)) % 2 == 0:
        N = N + '00'
    else:
        N = N + '10'
    if int(N, 2)>154:
        print(int(N, 2), i)
        break
for i in range(100,1000):
    N = sorted(map(str,str(i)))
    a1 = int(N[0]+N[1])
    a2 = int(N[2]+N[1])
    if a2-a1==60:
        print(i)
        break

