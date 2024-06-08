f = open('7390.txt')
a = [x for x in f]
k = 555  # 514
s = []
for i in range(len(a) - 1):
    if ((a[i])[-2] == '4') != ((a[i + 1])[-2] == '4'):
        if (int(a[i]) + int(a[i + 1])) % k != 0: s.append(int(a[i]) + int(a[i + 1]))
print(len(s), max(s))
