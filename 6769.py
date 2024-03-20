def F(x, h):
    if x>=111 and h == 2: return True
    if x < 111 and h < 4:
        a = F(x + 3, h + 1),F(x + 1, h + 1),F(x * 4, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False
for s in range(1, 110):
    if F(s, 0):
        print(s)