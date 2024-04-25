def chk(A):
    for X in range(-1000, 5000):
        if not(not((X & 123 != 0) or (X & 98 != 0)) or (not(X & 75 == 0) or (X & A != 0))):
            return False
    return True
for A in range(10000):
    if chk(A):
        print(A)
        break