for i in '0123456789ABCDEFGHI':
    s = '3' + i + '2' + i + '1' + i + '0' + i + '1'
    ss = i + '2024'
    sss = '1' + i + '077'
    k = int(s, 19) + int(ss, 19) + int(sss, 19)
    if k % 18 == 0:
        print(k // 18, i)

