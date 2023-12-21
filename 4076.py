a = 7**1003 + 6*7**1104 - 3*7**57 + 294
res = []
while a > 0:
    res.append(a % 7)
    a //= 7
print(sum(res))
