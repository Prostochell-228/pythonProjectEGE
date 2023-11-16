h = []
for i in range(4, 200):
    N = bin(i)
    N = N[2:]
    if i % 3 == 0:
        N = N + '010'
    else:
        g = bin((i % 3) * 5)[2:]
        N = N + g
    if int(N, 2) > 300 and int(N, 2)%2==0:
        h.append([int(N, 2), i])
print(min(h)[1])

