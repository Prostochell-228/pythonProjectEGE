f = open('6868b.txt')
h = int(f.readline())
a = [int(x) for x in f]
a = a + a
MM = -10 ** 10
ts = 0
for i in range(h + h // 2):
    ts += a[i]
    MM = max(MM, ts, a[i])
    if ts < a[i]: ts = a[i]
print(MM)
