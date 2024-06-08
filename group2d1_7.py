def ch(A):
    P = [x for x in range(2,10+1)]
    Q = [x for x in range(6,14+1)]
    for x in range(20):
        if ((not(x in A) or (x in P)) or (x in Q)):
            return True


for i in range(2, 16):
    i = [x for x in range(i, 16 + 1)]
    if ch(i):
        print(i)
