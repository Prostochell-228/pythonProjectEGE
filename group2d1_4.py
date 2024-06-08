def ch(A):
    for x in range(2000):
        for y in range(2000):
            if (4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < A):
                return False
    return True


for i in range(-2000,2000):
    if ch(i):
        print(i)
