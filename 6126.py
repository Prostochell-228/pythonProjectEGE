for x in range(215):
    a = (x * (215 ** 3)) + (7 * (215 ** 2)) + (5 * (215 ** 1)) + (1 * (215 ** 0))
    b = (2 * (215 ** 3)) + (3 * (215 ** 2)) + (7 * (215 ** 1)) + (x * (215 ** 0))
    if (a + b) % 567 == 0:
        print((a+b) // 567)