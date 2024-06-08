for i in range(0, 10 ** 8 + 1, 3377):
    x = str(i)
    if len(x) >= 6 and x[1] == '7' and x[2] == '9' and x[4] == '8' and x[-1] == '3':
        print(i, i / 3377)
