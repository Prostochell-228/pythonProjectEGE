# 2837 2579 2387
def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


a = []
s = 0
for x in range(298435, 363250):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            if i != (x // i):
                if test(i) and test(x // i):
                    a.append(x)
s = sum(a) / len(a)
s = round(s)
b = []
for i in a:
    b.append(abs(i - s))
d = b.index(min(b))
print(len(a),a[d])
