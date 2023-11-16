f = open('2668test.txt')
b = f.readline()
a = [int(line) ** 2 for line in f]
mindo = 100001
res = 100001
for i in range(5, len(a)):
    mindo = min(mindo, a[i - 5])
    res = min(res, a[i] + mindo)
print(res)
#2669