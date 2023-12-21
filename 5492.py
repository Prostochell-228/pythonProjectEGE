for i in '0123456789ABC':
    l1 = '8' + i + '121'
    l2 = '7' + i + '575'
    a = int(l1, 13) - int(l2, 13)
    if a%19==0:
        print(a//19)
