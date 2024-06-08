f = open('group3d4_2a.txt')
a = list(map(int, (f.readline()).split()))
x = [int(x) for x in f]
maxc = 0
maxs = 0
res = 0
for i in range(2*a[1], len(x)):
    maxc = max(maxc, x[i-2*a[1]])
    maxs = max(maxs, maxc+x[i-a[1]])
    res = max(res, maxs+x[i])
print(res)
#280212 26997