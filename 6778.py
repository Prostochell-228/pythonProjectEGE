def D(n, stop):
    if n == stop: return 1
    if n > stop or n == 17: return 0
    if n < stop: return D(n + 2, stop) + D(n + 3, stop)+ D(n * 2, stop)


print(D(3, 10)* D(10, 25))
