def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def test2(x):
    z = 1
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            z+=1
    return z
#1
b = [11,13,22,34,45]
a = b.copy()
for i in a:
    if test(i):
        b.remove(i)
print(b)
#2
s = []
for i in b:
    s.append([test2(i), i])
print(((sorted(s))[0])[1])
#3
a = [13,4,26,23,46]
for i in a:
    dv=0
    tr=0
    dva=0
    if i%26==0:
        dv+=1
        continue
    if i%13==0:
        tr+=1
        continue
    if i%2==0:
        dva+=1
        continue
print(dv*len(a)+(tr*dva))

