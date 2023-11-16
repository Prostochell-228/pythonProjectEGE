# 3
a = []
b = []

#1
for x in range(180131, 180179):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            b.append((x // i))
            b.append(i)
    if len(set(b))==4:
        a.append([max(b), x])
    b = []
print(a)

#2
p = [1 for  i in range(10**6)]
p[0] = 0
p[1] = 0
for i in range(2, 10**3):
    for k in range(i**2, 10**6, i):
        p[k] = 0
print(sum(map(lambda x: x[0], filter(lambda x: x[1], enumerate(p[1060: 18814], 1060)))))
