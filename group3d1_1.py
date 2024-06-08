f = open('day1_3_1.txt')
a = (f.readline()).split()
a = [int(a[0]), int(a[1])]
x = sorted([int(x) for x in f])
c = a[0]
s = 0
for i in x:
    if c - i > 0:
        s += 1
        c -= i
    else:
        print(s,i+c)
        break
