for i in range(1,200):
    a = 27**7 - 3**11 + 36 - i
    res = ''
    while a > 0:
        res += str(a % 3)
        a //= 3
    a = sum(map(int, res[::-1]))
    if a == 22:
        print(i)
        break
