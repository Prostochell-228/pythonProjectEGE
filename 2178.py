a = 3 * 16 ** 8 - 4 ** 5 + 3
res = ''
while a > 0:
    res = res + str(a % 4)
    a = a // 4
res = reversed(res)
print(res.count('3'), res)
