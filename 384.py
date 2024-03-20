for A in range(1, 1000):
    k=0
    for x in range(1, 1000):
        if not (x % 15 == 0 and not (x % 21 == 0)) or (not (x % A == 0) or not (x % 15 == 0)):
            k+=1
    if k==999: print(A)