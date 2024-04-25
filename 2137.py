def F(n):
    while '1111' in n:
        n = n.replace('1111', '2')
        n = n.replace('222', '1')
    return n


print(F(('1' * 46) + ('2' * 31)))
