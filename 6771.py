def F(x, y, h):
    if (x ** 2 + y ** 2) ** 0.5 > 14.0 and (h == 2 or h==4): return True
    if (x ** 2 + y ** 2) ** 0.5 <= 14.0 and h < 4:
        a = F(x, y + 4, h + 1), F(x * 2, y, h + 1), F(x, y + 3, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False


for s in range(1, 13 + 1):
    if F(3, s, 0):
        print(s)
