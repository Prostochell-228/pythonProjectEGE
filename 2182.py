def F(n):
    j = ''
    while n > 0:
        j = str(n % 3) + j
        n = n // 3
    return j


print(F(2*(27**7) + 3**10 - 9).count('0'))
