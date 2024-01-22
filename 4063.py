a = 7**103 + 6*7**104 - 3*7**57 + 98
res = ''
while a > 0:
    res += str(a % 7)
    a //= 7
print(res.count('6'))