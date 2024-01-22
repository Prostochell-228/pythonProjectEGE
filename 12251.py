def F(x, h):
    if x >= 301 and (h == 2 or h==4): return True
    if x < 301 and h < 4:
        a = F(x + 3, h + 1), F(x * 5, h + 1)
        if h % 2 == 0: return all(a)
        if h % 2 != 0: return any(a)
    return False


for s in range(1, 300 + 1):
    if F(s, 0):
        print(s)

