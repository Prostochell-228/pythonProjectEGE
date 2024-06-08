def ch(A):
    for x in range(2000):
        if not (not (x % 10 == 0 and x % 26 == 0 and (x >= 300)) or (A <= x)):
            return False
    return True


for i in range(200000):
    if ch(i):
        print(i)
#390