for i in range(200):
    n = bin(i)[2::]
    if i % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'
    if int(n,2)>516:
        print(i)