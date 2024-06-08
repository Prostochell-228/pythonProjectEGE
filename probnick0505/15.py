def f(A):
    for x in range(2000):
        for y in range(2000):
            if not((x >= 20) or (y >= 40) or (y <= (x + A)) or (y >= (3 * x - A))):
                return False
    return True
for i in range(200):
    if f(i):
        print(i)