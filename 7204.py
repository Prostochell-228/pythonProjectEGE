def F(n, stop):
    if n == stop: return 1
    if n > stop or n == 20: return 0
    if n < stop: return F(n + 1, stop) + F(n + 3, stop) + F(n ** 2, stop)


print(F(2, 15) * F(15, 35))
