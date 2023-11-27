def F(n):
    if n<=3:
        return n
    elif 3<n<=32:
        return n // 4 + F(n-3)
    elif n>32:
        return 2*F(n-5)
print(F(100))