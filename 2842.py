b = []
a = []
s = 0
def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
for x in range(round(12034679**0.25), round(23175821**0.25)):
        if test(x):
            a.append(x)
for i in a:
    if i**4 in range(12034679,23175821):
        b.append([i**3, i**4])
print(b)
