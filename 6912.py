h = []
for N in range(1000, 10000):
    b = oct(N)[2:]
    for x in "0246":
        b = b.replace(x, '1')
    b = b + str(N%8)
    for x in "0246":
        b = b.replace(x, '1')
    b = b + str(N%8)
    R = int(b, 8)
    if R%234==0: h.append(R)
print(max(h))