def ch(A):
    for x in range(2000):
        if not (not ((x & 156 != 0) or (x & 436 != 0)) or (x & A > 0)):
            return False
    return True


for i in range(2000):
    if ch(i):
        print(i)
