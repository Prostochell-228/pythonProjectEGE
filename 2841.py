b = []
a = []
s = 0
def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
for x in range(round(106732567**0.25), round(152673836**0.25)):
        if test(x):
            a.append(x)
for i in a:
    if i**4 in range(106732567,152673836):
        b.append([i**4, i**3])
print(sorted(b))
