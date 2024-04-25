h  = []
for i in range(500):
    N = bin(i)[2::]
    b = str((N.count('1'))%2)
    N = N+b
    b = str((N.count('1')) % 2)
    N = N + b
    if int(N,2)>=90 and int(N,2)<=160:
        h.append(int(N,2))
print(len(h))