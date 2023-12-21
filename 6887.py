def tree(n):
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return res[::-1]


h = []
for i in range(11, 300):
    n = tree(i)
    print(n)
    if n.count('1') < n.count('0') + n.count('2'):
        n = '22' + n
    else:
        n = '11' + n
    if int(n, 3) > 100:
        h.append(int(n, 3))
print(min(h))