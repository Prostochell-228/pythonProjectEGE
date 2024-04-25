def F(A):
    for x in range(2000):
        for y in range(2000):
            if not((x**2 + y**2 > 1024 - x) or (y < -2*x + A)):
                return False
    return True
for A in range(1000):
    if F(A):
        print(A)
        break