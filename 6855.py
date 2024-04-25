def F(a):
    while ('12' in a) or ('322' in a) or ('222' in a):
        if '12' in a:
            a = a.replace('12', '2', 1)
        if '322' in a:
            a = a.replace('322', '21', 1)
        if '222' in a:
            a = a.replace('222', '3', 1)
    return len(a)


h = []
for i in range(3, 1001):
    a = '1' + ('2' * i)
    h.append(F(a))
print(max(h))
