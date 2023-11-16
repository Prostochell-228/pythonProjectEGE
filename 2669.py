f = open('2669.txt')
b = f.readline()
a = [int(line) for line in f]
mindo = 100001
res = 100001
for i in range(6, len(a)):
    if a[i - 6] % 2 != 0:
        mindo = min(mindo, a[i - 6])
    if a[i] % 2 != 0:
        res = min(res, a[i] * mindo)
print(res)

