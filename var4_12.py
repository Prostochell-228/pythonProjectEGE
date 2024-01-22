def F(n):
    while '555' in n or '11' in n or '2' in n:
        if '555' in n:
            n = n.replace('555', '1')
        if '1' in n:
            n = n.replace('11', '25')
        if '2' in n:
            n = n.replace('2', '5')
    return n
for i in range(101,1000):
    g = '5'*i
    k = F(g)
    if k=='15':
        print(i)
        break
print(F('5'*104))