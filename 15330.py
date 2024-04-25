def F(A):
    B = [x for x in range(24, 91)]
    C = [x for x in range(47, 115)]
    for x in range(2000):
        if not(x in C) or (not(not(x in A) and (x in B)) or not(x in C)):
            return A
        else:
            return []
for i in range(200):
    A = [x for x in range(i)]
    h = F(A)
    print(len(h))
