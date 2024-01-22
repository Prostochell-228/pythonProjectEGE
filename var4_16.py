def F(n):
    if n < 2: return 1
    if n >= 2:
        if n % 3 == 0:
            return F(n / 3) - 1
        else:
            return F(n - 1) + 17


for i in range(20000000):
    if F(i) == 110:
        print(i)
