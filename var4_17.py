f = open('var4_17.txt')
a = [int(x.replace('\n', '')) for x in f]
j = []


def F(n, n2, n3):
    Flag = False
    Flag2 = False

    nn = list(map(int, str(n)))
    nn2 = list(map(int, str(n2)))
    nn3 = list(map(int, str(n3)))
    for i in range(4):
        if nn[i] == nn2[i]:
            Flag = not (Flag)
    for i in range(4):
        if nn2[i] == nn3[i]:
            Flag2 = not (Flag)
    f = Flag or Flag2
    return f


b = a.copy()
b = sorted(b)[::-1]
Max = b[0] + b[1]
for i in range(len(a) - 2):
    k = [a[i], a[i + 1], a[i + 2]]
    if sum(k) < Max and F(a[i], a[i + 1], a[i + 2]):
        j.append(sum(k))
print(min(j), len(j))
