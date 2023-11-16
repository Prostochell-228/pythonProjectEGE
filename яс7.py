h = []
for N in range(131, 256):
    b = bin(N)[2:].zfill(8)
    k = (len(b) - 4) // 2
    b1 = b[:k]
    b2 = b[len(b)-k:]
    b = b1+b2
    if int(b,2)==10: print(N); break

