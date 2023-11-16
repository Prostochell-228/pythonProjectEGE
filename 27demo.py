f = open('27_B_10108.txt')
K = int(f.readline())
N = int(f.readline())
a = []
for i in f:
    a.append(int(i))
max_s, max1, max2 = 0, 0, 0
for i in range(2*K,len(a)):
    max1 = max(max1, a[i - K - K])
    max2 = max(max2, a[i - K] + max1)
    max_s = max(max_s, a[i] + max2)
print(max_s)
