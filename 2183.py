def F(n):
    j = ''
    while n > 0:
        j = str(n % 5) + j
        n = n // 5
    return j


print(sum(map(int,F(4*(25**4) - 5**4 + 14))))
