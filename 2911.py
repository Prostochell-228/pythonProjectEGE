def F(n):
    s = []
    for i in range(2, round(n ** 0.5)):
        if n % i == 0:
            s.append(n // i)
        if len(s)>2:
            return []
    if len(s)==2:
        return s
    else:
        return []
for i in range(143146, 143215):
    g = F(i)
    if g:
        print(sorted(g))