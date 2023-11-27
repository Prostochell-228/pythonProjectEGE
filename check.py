for i in range(200):
    N = bin(i)[2:]
    if int(N) % 2 == 0:
        N = N + '01'
    else:
        N = N + '10'
    if int(N, 2)>154:
        print(int(N, 2), i)
        break
