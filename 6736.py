def F(n):
    while '555' in n or '11' in n or '2' in n:
        if '555' in n:n = n.replace('555', '1')
        if '11' in n:n = n.replace('11', '25')
        if '2' in n:n = n.replace('2', '5')
    return n
for i in range(100, 200):
    if F('5'*i)=='15':
        print(i)
        break
