for i in range(222):
    N = bin(i)[2:]
    print(N)
    if N.count('1') % 2 == 0:
        N += '0'
    else:
        N += '1'
    if int(i) % 2 == 0:
        N += '1'
    else:
        N += '0'
    if int(N, 2) > 204:
        print(i, int(N, 2), N)
        break
