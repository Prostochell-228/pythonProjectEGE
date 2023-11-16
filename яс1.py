h = []
for N in range(200):
    b = bin(N)[2:]
    N5 = N % 5
    if N5 == 0:
        k = b[len(b) - 3:]
        b = b + k
    else:
        N5 *= 5
        b = bin(N5)[2:] + b
    R = int(b, 2)
    if R > 512: print(N); break
