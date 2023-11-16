h = []
for N in range(2,256):
    b = bin(N)[2:].zfill(8)
    b = b[:len(b) - 1]
    b = b[::-1]
    R = int(b, 2)
    if R == N and R<100: print(N);
