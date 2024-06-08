a = (open('24var04.txt').readline()).split('E')
h = []
for i in a:
    h.append([len(i), i.count('A'), i])
a = sorted(h)[-1]
print(a)
s = 0
ss  = 0
print(a[2].count('A'))
for i in a[2]:
    s += 1
    if i == 'A' and ss<700:
        ss+=1
    if ss >=700:
        break
print(s)
print((a[2])[1402:])
