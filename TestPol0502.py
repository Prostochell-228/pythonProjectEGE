def D(n, stop):
    if n == stop: return 1
    if n > stop: return 0
    if n < stop: return D(n + 1, stop) + D(n * 2, stop)


print(D(3, 19))
