f = open('3147b.txt')
N = int(f.readline())
a = [list(map(int, i.split())) for i in f]

kucha = 1 - (sum(map(sum, a)) % 2)

b = [10 ** 1000, 10 ** 1000]
b[a[0][0] % 2] = a[0][0]
b[a[0][1] % 2] = min(b[a[0][1] % 2], a[0][1])
b[a[0][2] % 2] = min(b[a[0][2] % 2], a[0][2])

for i in a[1:]:
        k = [i[0] + b[0], i[1] + b[0], i[2] + b[0]]
        kk = [i[0] + b[1], i[1] + b[1], i[2] + b[1]]
        kkk = []
        if b[0] != 10 ** 1000: kkk += k
        if b[1] != 10 ** 1000: kkk += kk
        b[0] = min(list(filter(lambda x: x % 2 == 0, kkk)) + [10 ** 1000])
        b[1] = min(list(filter(lambda x: x % 2 == 1, kkk)) + [10 ** 1000])

print(b[kucha])
