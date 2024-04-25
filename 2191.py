def F(n):
    j = ''
    while n > 0:
        j = str(n % 9) + j
        n = n // 9
    return j


print(F(81**5 + 3**30 - 27).count('8'))
