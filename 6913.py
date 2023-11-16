h = []
for N in range(10000, 100000):
    b = oct(N)[2:]
    for x in "1357":
        b = b.replace(x, '2')
    b = b + str(N % 8)
    for x in "1357":
        b = b.replace(x, '2')
    b = b + str(N % 8)
    R = int(b, 8)
    if R%2023==0: h.append(N)
print(sum(h))
