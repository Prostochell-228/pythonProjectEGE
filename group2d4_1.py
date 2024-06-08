def F(n):
    while '71' in n or '72' in n or '73' in n:
        if '71' in n:
            n = n.replace('71', '227', 1)
        if '72' in n:
            n = n.replace('72', '37', 1)
        if '73' in n:
            n = n.replace('73', '17', 1)
    return n


for i in range(2000):
    print(i)
    if sum(map(int,F('7' + ('1') * (i + 1) + ('2') * (i + 2) + ('3') * (i + 3)))) == i * 9:
        print(i)
        break
