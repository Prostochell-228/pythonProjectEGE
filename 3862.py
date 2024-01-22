for i in range(200):
    a = 64 ** 11 - 4 ** 10 + 96 - i
    res = ''
    while a > 0:
        res += str(a % 4)
        a //= 4
    a = sum(map(int, res[::-1]))
    if a == 71:
        print(i)
        break
