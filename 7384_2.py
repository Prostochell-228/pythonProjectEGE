def F(s, h, k):
    if h == 3 and s >= 61 and k >= 0: return True
    if h < 3 and s < 61 and k >= 0:
        a = F(s + 1, h + 1, k - 1), F(s * 2, h + 1, k - s)
        if h % 2 == 0:
            return any(a)
        if h % 2 != 0:
            return all(a)
    return False


h = []
for s in range(1, 61):
    if F(s, 0, 80 - s):
        h.append(s)
print(h)
