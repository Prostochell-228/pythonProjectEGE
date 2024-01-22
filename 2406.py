def F(x, y, h):
    if x + y >= 65 and (h == 2 or h==4): return True
    if x + y < 65 and h < 4:
        a = F(x + 2, y, h + 1), F(x, y + 2, h + 1), F(x * 2, y, h + 1), F(x, y * 2, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False


for s in range(1, 59 + 1):
    if F(5, s, 0):
        print(s)
