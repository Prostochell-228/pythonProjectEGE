def F(n):
    while '56' in n or '3333' in n:
        n = n.replace('56', '3')
        n = n.replace('3333', '3')
    return n
print(F('563'*121))
