def F(x, y, h):
    if x + y >= 342 and (h == 2): return True
    if x + y < 342 and h < 2:
        a = F(x + 2, y, h + 1), F(x, y + 2, h + 1), F(x * 5, y, h + 1), F(x, y * 5, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False


for s in range(1, 325 + 1):
    if F(11, s, 0):
        print(s)
    