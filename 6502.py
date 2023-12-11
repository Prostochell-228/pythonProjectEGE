def F(x, stop, p, n):
    if (x == stop) and (p <= 6) and ('37' in n): return 1
    if (p > 6) or x > stop or x == 20 or x == 58: return 0
    if (x > 37) and ('37' not in n): return 0
    if x < stop:
        nt = ' ' + str(x)
        return F(x + 1, stop, p + 1, n) + F(x + 3, stop, p, n) + F(x * 3, stop, p, n)


print(F(3, 95, 0, ""))
