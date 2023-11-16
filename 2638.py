f = open('2638.txt')
b = f.readline()
a = [int(line) for line in f]
g = 0
a = sorted(a)[::-1]
j = 100
for i in range(100):
    g += ((a[i]) - (a[i] * 0.8))
print(g)
print(a[100])
