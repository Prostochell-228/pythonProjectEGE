def F(n):
    a = 572
    res = ''
    while a > 0:
        res = res + str(a % n)
        a = a // n
    res = res[::-1]
    return res


for i in range(2, 10):
    h = F(i)
    if len(set(h))<len(h):
        print(h, i)
print(2+3+4+7)