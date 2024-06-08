for n in range(200):
    i = bin(n)[2::]
    if i.count('1') % 2 == 0:
        i += '00'
    else:
        i += '10'
    if int(i, 2) > 77:
        print(n)
        break
