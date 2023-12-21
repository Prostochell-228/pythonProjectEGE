h = set()


def F(x, k):
    if k == 4: h.add(x)
    if k < 4:
        F(x + 2, k + 1)
        F(x * 3, k + 1)


F(1, 0)
print(len(h))
