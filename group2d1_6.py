def ch(A):
    for x in range(2000):
        for y in range(2000):
            if not((x + 2 * y > A) or (y < x) or (x < 30)):
                return False
    return True


for i in range(2000):
    if ch(i):
        print(i)
#89