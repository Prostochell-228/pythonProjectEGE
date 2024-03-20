def F(A):
    for x in range(1, 1000):
        if not(not(x % A == 0 and not (x % 15 == 0)) or ((x % 18 == 0) or (x % 15 == 0))):
            return False
    return True
for A in range(1, 1000):
    if F(A): print(A); break