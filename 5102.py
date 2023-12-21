h = []
for i in range(2000):
    N = bin(i)[2:]
    if i%2==0:
        N = '1'+N+'11'
    else:
        N = '11' + N + '0'
    if int(N,2) in range(500,1001):
        h.append(i)
print(h, len(h))