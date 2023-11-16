P = [x for x in range(5, 55)]
Q = [x for x in range(50, 94)]
A = 54
h = 0
while True:
    A += 1
    for i in range(54, 94):
        if not (i not in P and i in Q) or (i > A):
            h += 1
    if h == 20:
        print(A)
        break
    h = 0
