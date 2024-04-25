for i in range(512, 4095 + 1):
    n = str(i)
    j = [int(n[0]) + int(n[-1]), int(n[1]) + int(n[2])]
    k = str(min(j)) + str(max(j))
    if int(k) == 317:
        print(i)
