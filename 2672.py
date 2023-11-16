f = open('2672.txt')
b = f.readline()
a = [int(line) for line in f]
k6 = 0
k2 = 0
k3 = 0
for i in a:
    if i % 6 == 0:
        k6 += 1
    elif i % 2 == 0 and i % 3 != 0:
        k2 += 1
    elif i % 3 == 0 and i % 2 != 0:
        k3 += 1
a = (k6 * (k6 - 1))//2 + k6 * (len(a)-k6) + k2 * k3
print(a)
#кегэ - 9757