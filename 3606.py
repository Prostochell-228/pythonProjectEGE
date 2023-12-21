def F(n, stop, k):
    if n == stop:
        if k <= 5:
            return 1
        else:
            return 0
    if k > 5: return 0
    if n < stop: return 0
    if n > stop: return F(n + 1, stop, k + 1) + F(n * 2, stop, k + 1) + F(n + (n % 4), stop, k + 1)


h = []
for i in range(1,81):
    if F(i, 80, 0) > 0: h.append(i)
print(len(h))
