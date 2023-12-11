def F(x, stop):
    if x == stop: return 1
    if x > stop or x == 13: return 0
    if x < stop: return F(x + 1, stop) + F(x * 2, stop) + F(x * 3, stop)


print(F(3, 8)*F(8, 18))