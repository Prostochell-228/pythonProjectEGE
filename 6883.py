h = []


def fif(N):
    j = ''
    while N > 0:
        j = str(N % 5) + j
        N = N // 5
    return j


for N in range(5, 50):
    b = fif(N)
    if N % 5 == 0:
        b = b + b[-2:]
    else:
        k = (N % 5) * 7
        k = fif(k)
        b = b + k
    R = int(b, 5)
    if R > 200: h.append(R)
print(sorted(h))
