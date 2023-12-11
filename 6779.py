def F(x, stop):
    if x == stop: return 1
    if x < stop or x == 9 or x == 16: return 0
    if x > stop: return F(x - 1, stop) + F(x - 2, stop) + F(x // 3, stop)


print(F(19, 3))