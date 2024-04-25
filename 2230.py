def F(n):
    j = ''
    while n > 0:
        j = str(n % 3) + j
        n = n // 3
    return j


print(F(9**17 + 3**16 - 27).count('0'))
print(F(9**17 + 3**16 - 27).count('1'))
print(F(9**17 + 3**16 - 27).count('2'))
