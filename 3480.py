def F(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x-30<A) and (15-y<A)) or (x*(y+3)>60)):
                return False
    return True
for A in range(1, 1000):
    if F(A): print(A); break