def f(n):
    while '31' in n or '411' in n or '1111' in n:
        if '31' in n:
            n  = n.replace('31', '1', 1)
        if '411' in n:
            n = n.replace('411', '13', 1)
        if '1111' in n:
            n = n.replace('1111', '4', 1)
    return sum(list(map(int, n)))

for i in range(3, 10001):
    k = ('4' + '1' * i)
    l = f(k)
    if l==34:
        print(i)