h = []
for N in range(20,601):
    b = bin(N)[2:]
    b = b[:len(b) - 2]
    h.append(int(b, 2))
print(len(set(h)))