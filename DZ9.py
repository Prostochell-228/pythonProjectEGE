import itertools


def svn(N):
    j = ''
    while N > 0:
        j = str(N % 7) + j
        N = N // 7
    return j


def prs(i):
    for a in range(2, round(i ** 0.5) + 1):
        if i % a == 0:
            return False
    return True


h = []
for i in range(343, 2402):
    H = svn(i)
    if int(H[-1]) % 2 == 0:
        H = '6' + H
    else:
        H = '5' + H
    if int(H, 7) > 14500:
        h.append(int(H, 7))
print(len(h))
hh = 0
k = []
h = []
for i in range(100, 1000):
    for line in itertools.product(str(i), repeat=2):
        h.append(int((line[0] + line[1])))
    l = set(h)
    j = l.copy()
    for i in j:
        if prs(i):
            hh+=1
        else:
            l.remove(i)
    k.append([len(l), i])
    h = []
print(sorted(k))
