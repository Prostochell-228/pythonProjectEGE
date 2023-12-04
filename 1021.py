def F(n):
    if n <= 2:
        return G(n)
    else:
        return G(n) + F(n - 2)


def G(n):
    if n <= 2:
        return n
    else:
        return F(n - 1) - G(n - 2)
print(G(15))