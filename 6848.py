h = []
for N in range(800, 4095):
    b = str(N)
    j = b[-1]
    k = b[0]
    h = b[1]
    l = b[2]
    h.append((int(j) + int(k)))
    h.append((int(h) + int(l)))
    
