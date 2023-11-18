h = []
for N in range(200):
    b = bin(N)[2:]
    N5 = N % 4
    if N5 == 0:
        k = b[len(b) - 2:]
        b = b + k
    else:
        b = b + bin(N5)[2:]
    if b[-1]==0:
        b = b[1 :]
    R = int(b, 2)
    if R > 213: print(R); break
