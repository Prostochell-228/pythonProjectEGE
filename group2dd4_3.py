def F(n):
    n = bin(n)[::2]
    if n.count('1') % 2 == 0:
        n = '1' + n + '00'
    else:
        n = '11' + n
    if int(n, 2) >= 412:
        return True


for i in range(2000):
    if F(i):
        print(i)
        break
