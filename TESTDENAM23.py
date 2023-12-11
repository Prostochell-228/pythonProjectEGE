def F(n, stop, s):
    if n == stop:
        if s[-2] == '1':
            return 1
        else:
            return 0
    if n > stop: return 0
    if n < stop: return F(n + 1, stop, s + '1') + F(n * 2, stop, s + '2')


print(F(3, 20, ''))


def D(n, stop):
    if n == stop: return 1
    if n > stop: return 0
    if n < stop: return D(n + 1, stop) + D(n + 2, stop)+ D(n * 2, stop)


print(D(1, 7) * D(7, 10)* D(10, 12))
