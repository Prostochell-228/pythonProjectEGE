f = open('2642.txt')
b = f.readline()
a = [int(line) for line in f]
a = sorted(a)[::-1]
s = 0
b = a.copy()

for i in range(len(b)):
    if b[i] + b[i + 1] >= 20000:
        s += 1
        if b[i] + b[i + 1] - 20000 != 0:
            a.append(a[i] - a[i + 1])
        a = a.remove(a[i])
        a = a.remove(a[i])
    else:
        c = 1
        h = 1
        g = b[i] + b[i + c]
        while g < 20000:
            g += a[i + c]
            c += 1
        h += c
        s+=h
        d = 0
        while d<c:
            a = a.remove(i)
            d+=1
print(s)
