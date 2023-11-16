for n in range(2, 300):
    n2 = bin(n)[2:]
    j = int(n2,2)
    if j % 2 != 0:
        n2 += '0'
    else:
        n2 = '1'+n2
    if n2.count('1') % 2 == 0:
        n2 += '1'
    else:
        n2 += '0'
    if int(n2, base=2) > 228:
        print(n)
        break
