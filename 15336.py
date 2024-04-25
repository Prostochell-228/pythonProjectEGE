def F(x, y, h):
    if x + y >= 123 and h == 4: return True
    if x + y < 123 and h < 4:
        a = F(x + 1, y, h + 1), F(x, y + 1, h + 1), F(x * 2, y, h + 1), F(x, y * 2, h + 1)
        if h % 2 == 0: return any(a)
        if h % 2 != 0: return all(a)
    return False


for s in range(1, 109 + 1):
    if F(13, s, 0):
        print(s)