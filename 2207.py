def F(n):
    j = ''
    while n > 0:
        j = str(n % 7) + j
        n = n // 7
    return j


print(F(8*(343**5) + 9*(49**8) - 48).count('6'))
