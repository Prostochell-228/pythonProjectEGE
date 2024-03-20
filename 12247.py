def F(A):
    for x in range(1, 1000):
        P = (x&A==0) or not(x&37==0) or not(x&12==0)
        if P == False: return False
    return True


for A in range(1, 1000):
    if F(A):
        print(A)





