def F(x, h):
    if x >= 84 and (h == 2 or h==4): return True
    if x < 84 and h < 4:
        if x % 2 != 0:
            a = F(x + 3, h + 1), F(x * 2, h + 1)
        else:
            xx = x/2
            a = F(x + 3, h + 1), F(x + xx, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False


for s in range(1, 83 + 1):
    if F(s, 0):
        print(s)
