for i in range(500):
    N = bin(i)[2::]
    b = str((N.count('1'))%2)
    N = N+b
    b = str((N.count('1')) % 2)
    N = N + b
    if int(N,2)>125:
        print(i, N, int(N,2))
        break