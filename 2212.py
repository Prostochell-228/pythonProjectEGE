def F(n):
    j = ''
    while n > 0:
        j = str(n % 3) + j
        n = n // 3
    return j


print(F(9**20 + 3**60 - 5).count('2'))
