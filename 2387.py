def F(x, y, h):
    if x + y >= 275 and (h == 2 or h==4): return True
    if x + y < 275 and h < 4:
        a = F(x + 3, y, h + 1), F(x, y + 3, h + 1), F(x * 4, y, h + 1), F(x, y * 4, h + 1), F(x + 7, y, h + 1), F(x, y + 7, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False


for s in range(1, 216 + 1):
    if F(58, s, 0):
        print(s)
