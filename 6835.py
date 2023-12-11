def F(x, stop):
    if x == stop: return 1
    if x > stop or x == 23: return 0
    if x < stop: return F(x + 2, stop) + F(x * 3, stop) + F(x * 5, stop)


print(F(1, 13)*F(13, 75))
