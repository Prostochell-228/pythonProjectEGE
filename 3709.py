def F(x, stop):
    if x == stop: return 1
    if int(x, 2) > int(stop, 2): return 0
    if int(x, 2) < int(stop, 2): return F(bin(int(x, 2) + 1)[2:], stop) + F(x + '0', stop) + F(x + '1', stop)


print(F('100', '11101'))
