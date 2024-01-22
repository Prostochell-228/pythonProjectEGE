import functools

f = open('4262.csv')
s = 0


@functools.lru_cache()
def delit(n):
    h = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            h.append(i)
            h.append(n // i)
    return h


for line in f:
    m = [int(x) for x in line.split()]
    j = max(m)
    m.remove(j)
    if m[0] ** 2 + m[1] ** 2 == j ** 2:
        h1 = delit(m[0])
        h2 = delit(m[1])
        h3 = delit(j)
        hh = h1 + h2 + h3
        hhs = set(hh)
        if len(hhs) == len(hh):
            s += 1
print(s)
