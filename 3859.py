for i in range(1, 200000):
    a = 64 ** 12 - 8 ** 14 + i
    res = ''
    while a > 0:
        res += str(a % 8)
        a //= 8
    if res.count('7') == 12 and res.count('1') == 1:
        print(i)
        break
