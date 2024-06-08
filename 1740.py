
def F(i):
    n = bin(i)[::2]
    if n.count('1') % 2 == 0:
        n = n + '00'
    else:
        n = n + '10'
    if int(n, 2) < 86:
        print(int(n, 2))


for i in range(200000):
    F(i)