for i in range(4, 200):
    N = bin(i)
    N = N[2:]
    if i % 5 == 0:
        J = (N[2] + N[1] + N[0])
        N = N + J
    else:
        g = bin((i % 5)*5)[2:]
        N = N+g
    if int(N,2)>=256:
        print(int(N,2), i)
        break