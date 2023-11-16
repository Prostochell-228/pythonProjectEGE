for n in range(2, 300):
    n2 = bin(n)[2:]
    j = n2.count('1')
    if j % 2 == 0:
        n2 += '0'
        n2 = n2[2:]
        n2 = '10' + n2
    else:
        n2 += '1'
        n2 = n2[2:]
        n2 = '11' + n2
    if int(n2, 2) >= 16:
        print(int(n2, 2), n)
        break
