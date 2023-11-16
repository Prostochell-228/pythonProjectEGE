for N in range(20000):
    h = bin(N)[2:]
    k = h.count('1')
    if k%2==0:
        h = '1'+h+'00'
    else:
        h = '11'+h
    R = int(h, 2)
    if R == 412: print(N)