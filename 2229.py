def F(n):
    j = ''
    while n > 0:
        j = str(n % 3) + j
        n = n // 3
    return j


print(sum(map(int,F(9**8 + 3**25 - 14))))
