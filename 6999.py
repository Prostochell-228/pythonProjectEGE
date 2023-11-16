for N in range(200):
    h = bin(N)[2:]
    if h.count('0') == 0: continue
    pos = h.find('0')
    m = list(h)
    m[pos] = h[:2]
    h = "".join(m)
    h = h[::-1]
    R = int(h, 2)
    if R == 123: print(N)
