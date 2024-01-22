a = 103 * 7 ** 103 - 5 * 7 ** 57 + 98
res = ''
while a > 0:
    res += str(a % 7)
    a = a // 7
res = res[::-1]
print(sum(map(int,res)))
