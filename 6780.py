def D(n, stop):
    if n == stop: return 1
    if n < stop or n == 7: return 0
    if n > stop: return D(n - 1, stop) + D(n - 3, stop) + D(n // 2, stop)


print(D(19, 10) * D(10, 3))
