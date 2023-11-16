h = []
for N in range(20,2501):
    b = bin(N)[2:]
    b = b.replace('0','')
    h.append(int(b, 2))
print(len(set(h)))