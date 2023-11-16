s = 0
for i in range(8, 1000000):
    N = oct(i)
    N = N[2:]
    if i % 7 == 0:
        J = (N[-2] + N[-1])
        N = N + J
    else:
        g = oct((i % 7) * 7)[2:]
        N = N + g
    if int(N, 8) < 3000:
        s += 1
print(s)
