import fnmatch

h = []
def F(n):
    s = 0
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            s += 2
    return s + 2


for i in range(10 ** 6 + 1):
    if fnmatch.fnmatch(str(i), '4*') == True:
        if F(i)==24:
            h.append(i)
print(len(h), h)
